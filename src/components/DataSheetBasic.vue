<template>
  <div id="base-sheet">
    <div id="datasheet-header">
      <h1>{{jsonElementData.result.primaryTopic.label._value}}</h1>
      <h2 v-if="jsonElementData.result.primaryTopic.prefLabel.length > 0">
        <span
          v-for="(label, index) in jsonElementData.result.primaryTopic.prefLabel"
          v-bind:key="index"
        >{{label._value}}<span v-if="index != jsonElementData.result.primaryTopic.prefLabel.length -1">, </span></span>
      </h2>
      <h3 v-if="jsonElementData.result.primaryTopic._about != null">
        <a
          :href="jsonElementData.result.primaryTopic._about"
          target="_blank"
        >{{jsonElementData.result.primaryTopic._about}}</a>
      </h3>
    </div>
    <div id="table-container">
      <table>
        <tr v-if="jsonElementData.result.primaryTopic.notation != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
            content:'Notation  of ' + jsonElementData.result.primaryTopic.label._value + ' according to Geological Timescale (2018)', 
            class: 'tooltip',
            delay: 50
          }">Notation</span></th>
          <td class="value">
            <ul>
              <li>{{jsonElementData.result.primaryTopic.notation}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.comment != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
            content:'A description of the ' + jsonElementData.result.primaryTopic.label._value + '.', 
            class: 'tooltip',
            delay: 50
          }">Comments</span></th>
          <td class="value">
            <ul>
              <li
                v-for="(comment, index) in jsonElementData.result.primaryTopic.comment"
                v-bind:key="index"
              >{{comment._value}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.narrower != null">
           <th class="label"><span class="tooltip-text" v-tooltip.left="{
            content:'A list of smaller (child) intervals occuring within the ' + jsonElementData.result.primaryTopic.label._value + '.', 
            class: 'tooltip',
            delay: 50
          }">Interval Contains</span></th>
          <td class="value">
            <ul>
              <li>
                <table
                  class="nested-table"
                  v-for="(child, index) in jsonElementData.result.primaryTopic.narrower"
                  v-bind:key="index"
                >
                  <tr>
                    <th colspan="2" @click="updateData(child._about)">{{child.label._value}}</th>
                  </tr>
                  <tr>
                    <td class="label">Interval During</td>
                    <td class="value">{{jsonElementData.result.primaryTopic.label._value}}</td>
                  </tr>
                </table>
              </li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.broader != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
            content:'A list of larger (parent) intervals that the ' + jsonElementData.result.primaryTopic.label._value + ' belongs to.', 
            class: 'tooltip',
            delay: 50
          }">Interval During</span></th>
          <td class="value">
            <ul>
              <li>
                <table
                  class="nested-table"
                  v-for="(parent, index) in jsonElementData.result.primaryTopic.broader"
                  v-bind:key="index"
                >
                  <tr>
                    <th colspan="2" @click="updateData(parent._about)">{{parent.label._value}}</th>
                  </tr>
                  <tr>
                    <td class="label">Interval Contains</td>
                    <td class="value">{{jsonElementData.result.primaryTopic.label._value}}</td>
                  </tr>
                </table>
              </li>
              <li v-if="jsonElementData.result.primaryTopic.broaderTransitive != null">
                <table
                  class="nested-table"
                  v-for="(parent, index) in jsonElementData.result.primaryTopic.broaderTransitive"
                  v-bind:key="index"
                >
                  <tr>
                    <th colspan="2" @click="updateData(parent._about)">{{parent.label._value}}</th>
                  </tr>
                  <tr>
                    <td class="label">Interval Contains</td>
                    <td class="value">{{jsonElementData.result.primaryTopic.label._value}}</td>
                  </tr>
                </table>
              </li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.intervalStartedBy != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
            content:'The earliest child interval of the ' + jsonElementData.result.primaryTopic.label._value + '.', 
            class: 'tooltip',
            delay: 50
          }">Interval Started By</span></th>
          <td class="value">
            <ul>
              <li><a @click="updateData(jsonElementData.result.primaryTopic.intervalStartedBy._about)">{{jsonElementData.result.primaryTopic.intervalStartedBy.label._value}}</a></li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.intervalFinishedBy != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
            content:'The latest child interval of the ' + jsonElementData.result.primaryTopic.label._value + '.', 
            class: 'tooltip',
            delay: 50
          }">Interval Finished By</span></th>
          <td class="value">
            <ul>
              <li><a @click="updateData(jsonElementData.result.primaryTopic.intervalStartedBy._about)">{{jsonElementData.result.primaryTopic.intervalFinishedBy.label._value}}</a></li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.hasBeginning != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
            content:'The geochronologic boundary where the ' + jsonElementData.result.primaryTopic.label._value + ' started.', 
            class: 'tooltip',
            delay: 50
          }">Beginning</span></th>
          <td class="value">
            <ul>
              <li @click="getMoreData(jsonElementData.result.primaryTopic.hasBeginning._about)"><a>{{jsonElementData.result.primaryTopic.hasBeginning.label._value}}</a></li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.hasEnd != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
            content:'The geochronologic boundary where the ' + jsonElementData.result.primaryTopic.label._value + ' ended.', 
            class: 'tooltip',
            delay: 50
          }">End</span></th>
          <td class="value">
            <ul>
              <li @click="getMoreData(jsonElementData.result.primaryTopic.hasEnd._about)"><a>{{jsonElementData.result.primaryTopic.hasEnd.label._value}}</a></li>
            </ul>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>

import EventBus from "../assets/event-bus.js";
export default {
  name: "DataSheetBasic",
  props: {
    jsonElementData: Object,
  },
  methods: {
    getMoreData: function(url) {
      EventBus.$emit('get-more-data', url)
    },
    updateData: function(url) {
      var label = this.jsonElementData.result.primaryTopic.label._value
      EventBus.$emit('update-data', [url, label])
    }
  }
};
</script>


<style scoped>
p {
  text-align: center;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#datasheet-header {
  border: 3px solid lightgray;
  border: 0;
  padding: 10px;
  margin-bottom: 0;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 20px;
  background-color: #0c415a;
  color: white;
  margin-bottom: 0;
  border-bottom: 0;
}
#datasheet-header a {
  color: white;
  text-decoration: none;
  background-image: linear-gradient(white, white);
  background-position: 50% 100%;
  background-repeat: no-repeat;
  background-size: 0% 2px;
  transition: background-size 0.2s ease-in-out;
}
#datasheet-header a:hover {
  background-size: 100% 2px;
}
#base-sheet{
  height: 100%;
  width: 75%;
  margin-left: auto;
  margin-right: auto;
  background-color: white;
}
#table-container {
  border: 3px solid lightgray;
  border: 0;
  padding: 10px;
  margin-top: 0;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 20px;
  background-color: white;
}
table, td, th {
  border-top: 1px solid lightgrey;
  border-bottom: 1px solid lightgrey;
  border-collapse: collapse;
}
table {
  width: 100%;
}
td {
  width: 60%;
}
td li {
  display: block;
  text-align: left;
}
th {
  text-align: left;
  padding-left: 5%;
  padding-top: 16px;
  vertical-align: top;
  padding-right: 5%;
}
.value a{
  font-weight: 500;
  background-image: linear-gradient(#42B983, #42B983);
  background-position: 50% 100%;
  background-repeat: no-repeat;
  background-size: 0% 1px;
  transition: background-size 0.2s ease-in-out;
}
.value a:hover{
  background-size: 100% 1px;
  cursor: pointer;
}
.nested-table,
.nested-table td,
.nested-table th {
  border: 1px solid lightgrey;
  border-collapse: collapse;
}
.nested-table td {
  font-size: 0.9em;
  text-align: left;
  padding-left: 5%;
  padding-right: 5%;
}
.nested-table th {
  background-color: #dae2e6;
  padding-top: 10px;
  padding-bottom: 10px;
  transition: all 0.2s ease-in-out;
}
.nested-table th:hover {
  background-color: #bdd1db;
  cursor: pointer;
  text-decoration: underline 1px;
  padding-left: 30px;  
}

.nested-table .label {
  width: 40%;
}
</style>