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
      <stratotype-table v-if="stratotypeData != null && stratotypeData.length == 1" v-bind:stratotypeData="stratotypeData[0]"></stratotype-table>
      <div id="stratotype-tables" v-else-if="stratotypeData != null && stratotypeData.length > 1">
        <stratotype-table v-for="(data, index) in stratotypeData" v-bind:key="index" v-bind:stratotypeData="data" v-bind:sdHeading="index == 0"></stratotype-table>
      </div>
    </div>
  </div>
</template>

<script>
import EventBus from "../assets/event-bus.js";
import StratotypeTable from "./StratotypeTable.vue"
export default {
  name: "DataSheetTemporalEdge",
  props: {
    jsonElementData: Object,
    stratotypeData: Array
  },
  components: {
    StratotypeTable
  },
  methods: {
    clickBackButton: function() {
      EventBus.$emit('go-back', true)
    }
  },
  mounted(){
    console.log(this.stratotypeData[0])
  }
};
</script>


<style scoped>
#back-arrow{
  font-size: 68px;
  position: fixed;
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