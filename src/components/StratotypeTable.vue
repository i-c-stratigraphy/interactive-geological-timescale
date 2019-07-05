<template>
  <div class="stratotype-table-container">
      <h3 v-if="sdHeading">Stratotype Data</h3>
      <h3 v-else><br></h3>
      <h4 v-if="stratotypeData.result.primaryTopic._about != null"><a
          :href="stratotypeData.result.primaryTopic._about"
          target="_blank"
        >{{stratotypeData.result.primaryTopic._about}}</a></h4>
      <table v-if="stratotypeData != null">
        <tr v-if="stratotypeData.result.primaryTopic.label != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'The human readable name of this stratographic point.', 
              class: 'tooltip',
              delay: 50
            }">
            Label
          </span></th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.label._value}} ({{stratotypeData.result.primaryTopic.label._lang}})</li>
            </ul>
          </td>
        </tr>
        <tr>
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: (!stratotypeData.result.primaryTopic.ratifiedGSSP) ? 'The ' + stratotypeData.result.primaryTopic.label._value + ' has not been ratified by the ICS.' : 'The ' + stratotypeData.result.primaryTopic.label._value + ' has been ratified by the ICS.', 
              class: 'tooltip',
              delay: 50
            }">
            Ratified GSSP
          </span></th>
          <td class='value'>
            <ul>
              <li><span v-if="stratotypeData.result.primaryTopic.ratifiedGSSP == null || !stratotypeData.result.primaryTopic.ratifiedGSSP">&#x2718;</span><span v-else-if="stratotypeData.result.primaryTopic.ratifiedGSSP">&#x2714;</span></li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.status != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'The formal ICS status of the ' + stratotypeData.result.primaryTopic.label._value + ' (boundary and point).', 
              class: 'tooltip',
              delay: 50
            }">
            Formal ICS Status
          </span></th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.status}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.boundaryLevel != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'The level within the section of the point characterizing the boundary.', 
              class: 'tooltip',
              delay: 50
            }">
            Boundary Level
          </span></th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.boundaryLevel}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.correlationEvent != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'The stratigraphic event that is intended to be represented by the ' + stratotypeData.result.primaryTopic.label._value + '.', 
              class: 'tooltip',
              delay: 50
            }">
            Correlation Event
          </span></th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.correlationEvent}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.comment != null && !(stratotypeData.result.primaryTopic.comment instanceof Array)">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'A description of the ' + stratotypeData.result.primaryTopic.label._value + '.', 
              class: 'tooltip',
              delay: 50
            }">
            Comment
          </span></th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.comment._value}} ({{stratotypeData.result.primaryTopic.comment._lang}})</li>
            </ul>
          </td>
        </tr>
        <tr v-else-if="stratotypeData.result.primaryTopic.comment != null">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'A description of the ' + stratotypeData.result.primaryTopic.label._value + '.', 
              class: 'tooltip',
              delay: 50
            }">
            Comment
          </span></th>
          <td class='value'>
            <ul>
              <li v-for="(comment, index) in stratotypeData.result.primaryTopic.comment" v-bind:key="index">{{comment._value}} ({{comment._lang}})</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.source != null && (stratotypeData.result.primaryTopic.source instanceof Array)">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'Source(s) where the data about the ' + stratotypeData.result.primaryTopic.label._value + 'is derived.', 
              class: 'tooltip',
              delay: 50
            }">
            Source(s)
          </span></th>
          <td class='value'>
            <ul>
              <li v-for="(source, index) in stratotypeData.result.primaryTopic.source" :key="index">{{source}}</li>
            </ul>
          </td>
        </tr>
        <tr v-else-if="stratotypeData.result.primaryTopic.source != null && !(stratotypeData.result.primaryTopic.source instanceof Array)">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'Source(s) where the information about the ' + stratotypeData.result.primaryTopic.label._value + 'is derived.', 
              class: 'tooltip',
              delay: 50
            }">
            Source(s)
          </span></th>
          <td class='value'>
            <ul>
              <li>{{stratotypeData.result.primaryTopic.source}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="stratotypeData.result.primaryTopic.seeAlso != null && (stratotypeData.result.primaryTopic.seeAlso instanceof Array)">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'Resource(s) that are related to the ' + stratotypeData.result.primaryTopic.label._value + '.', 
              class: 'tooltip',
              delay: 50
            }">
            See Also
          </span></th>
          <td class='value'>
            <ul>
              <li v-for="(source, index) in stratotypeData.result.primaryTopic.seeAlso" :key="index"><a :href="source" target="_blank">{{source.split('/')[source.split('/').length - 1]}}</a></li>
            </ul>
          </td>
        </tr>
        <tr v-else-if="stratotypeData.result.primaryTopic.seeAlso != null && !(stratotypeData.result.primaryTopic.seeAlso instanceof Array)">
          <th class="label"><span class="tooltip-text" v-tooltip.left="{
              content: 'Resource(s) that are related to the ' + stratotypeData.result.primaryTopic.label._value + '.', 
              class: 'tooltip',
              delay: 50
            }">
            See Also
          </span></th>
          <td class='value'>
            <ul>
              <li><a :href="stratotypeData.result.primaryTopic.seeAlso" target="_blank">{{stratotypeData.result.primaryTopic.seeAlso.split('/')[stratotypeData.result.primaryTopic.seeAlso.split('/').length - 1]}}</a></li>
            </ul>
          </td>
        </tr>
      </table>
    </div>
</template>

<script>
import EventBus from "../assets/event-bus.js";
export default {
  name: "StratotypeTable",
  props: {
    stratotypeData: Object,
    sdHeading: {
      type: Boolean,
      default: true
    }
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
  -webkit-user-select: none;
  -moz-user-select: none;  
  -ms-user-select: none;  
  user-select: none;   
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
h4 a{
  text-decoration: none;
  background-image: linear-gradient(#42B983, #42B983);
  background-position: 50% 100%;
  background-repeat: no-repeat;
  background-size: 0% 2px;
  transition: background-size 0.2s ease-in-out;
}
h4 a:hover{
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