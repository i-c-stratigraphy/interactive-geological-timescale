<template>
  <div id="base-sheet">
    <div id="back-arrow" @click="clickBackButton">
      &#x1f844;
    </div>
    <div id="datasheet-header">
      <h1>{{jsonElementData.result.primaryTopic.label._value}}</h1>
      <h2 v-if="jsonElementData.result.primaryTopic.prefLabel.length > 0">
        <span
          v-for="label in jsonElementData.result.primaryTopic.prefLabel"
          v-bind:key="label._lang"
        >{{label._value}} /</span>
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
        <tr v-if="jsonElementData.result.primaryTopic.altLabel != null && jsonElementData.result.primaryTopic.altLabel.length > 0">
          <th class='label'>
            Alternate Label
          </th>
          <td class='value'>
            <ul>
              <li v-for="(label, index) in jsonElementData.result.primaryTopic.altLabel" :key="index">{{label._value}} ({{label._lang}})</li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.ratifiedGSSP != null">
          <th class='label'>
            Ratified GSSP
          </th>
          <td class='value'>
            <ul>
              <li><span v-if="jsonElementData.result.primaryTopic.ratifiedGSSP == null || !jsonElementData.result.primaryTopic.ratifiedGSSP">&#x2718;</span><span v-else-if="jsonElementData.result.primaryTopic.ratifiedGSSP">&#x2714;</span></li>
            </ul>
          </td>
        </tr>
      </table>
      <h3 v-if="stratotypeData != null">Stratotype Data</h3>
      <h4 v-if="stratotypeData != null"><a
          :href="stratotypeData.result.primaryTopic._about"
          target="_blank"
        >{{stratotypeData.result.primaryTopic._about}}</a></h4>
      <table v-if="stratotypeData != null">
        <tr v-if="stratotypeData.result.primaryTopic.label != null">
          <th class='label'>
            Label
          </th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.label._value}} ({{stratotypeData.result.primaryTopic.label._lang}})</li>
            </ul>
          </td>
        </tr>
        <tr>
          <th class='label'>
            Ratified GSSP
          </th>
          <td class='value'>
            <ul>
              <li><span v-if="stratotypeData.result.primaryTopic.ratifiedGSSP == null || !stratotypeData.result.primaryTopic.ratifiedGSSP">&#x2718;</span><span v-else-if="stratotypeData.result.primaryTopic.ratifiedGSSP">&#x2714;</span></li>
            </ul>
          </td>
        </tr>
        <tr>
          <th class='label'>
            Formal ICS Status
          </th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.status}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.boundaryLevel != null">
          <th class='label'>
            Boundary Level
          </th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.boundaryLevel}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.correlationEvent != null">
          <th class='label'>
            Correlation Event
          </th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.correlationEvent}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.comment != null">
          <th class='label'>
            Comment
          </th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.comment._value}} ({{stratotypeData.result.primaryTopic.comment._lang}})</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.source != null && (stratotypeData.result.primaryTopic.source instanceof Array)">
          <th class='label'>
            Source(s)
          </th>
          <td class='value'>
            <ul>
              <li v-for="(source, index) in stratotypeData.result.primaryTopic.source" :key="index">{{source}}</li>
            </ul>
          </td>
        </tr>
        <tr v-else-if="stratotypeData.result.primaryTopic.source != null && !(stratotypeData.result.primaryTopic.source instanceof Array)">
          <th class='label'>
            Source(s)
          </th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.source}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.seeAlso != null && (stratotypeData.result.primaryTopic.seeAlso instanceof Array)">
          <th class='label'>
            See Also
          </th>
          <td class='value'>
            <ul>
              <li v-for="(source, index) in stratotypeData.result.primaryTopic.seeAlso" :key="index"><a :href="source" target="_blank">{{source.split('/')[source.split('/').length - 1]}}</a></li>
            </ul>
          </td>
        </tr>
        <tr v-else-if="stratotypeData.result.primaryTopic.seeAlso != null && !(stratotypeData.result.primaryTopic.seeAlso instanceof Array)">
          <th class='label'>
            See Also
          </th>
          <td class='value'>
            <ul>
              <li><a :href="stratotypeData.result.primaryTopic.seeAlso" target="_blank">{{stratotypeData.result.primaryTopic.seeAlso.split('/')[stratotypeData.result.primaryTopic.seeAlso.split('/').length - 1]}}</a></li>
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
  name: "DataSheetTemporalEdge",
  props: {
    jsonElementData: Array,
    stratotypeData: Array
  },
  methods: {
    clickBackButton: function() {
      EventBus.$emit('go-back', true)
    }
  }
};
</script>


<style scoped>
#back-arrow{
  font-size: 68px;
  position: absolute;
  transition: opacity .5s;
  opacity: 0.25;
}
#back-arrow:hover{
  color: #0C415A;
  opacity: 1;
  cursor: pointer;
}
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
  width: 75%;
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

#table-container {
  border: 3px solid lightgray;
  border: 0;
  padding: 10px;
  margin-top: 0;
  width: 75%;
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
}
.nested-table .label {
  width: 40%;
}
</style>