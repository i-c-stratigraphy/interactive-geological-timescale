<template>
  <div id="base-sheet">
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
    </div>
  </div>
</template>

<script>
import EventBus from "../assets/event-bus.js";
export default {
  name: "DataSheetTemporalEdge",
  props: {
    jsonElementData: Array
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