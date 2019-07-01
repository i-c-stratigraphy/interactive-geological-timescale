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
        >{{jsonElementData.result.primaryTopic._about}}</a>
      </h3>
    </div>
    <div id="table-container">
      <table>
        <tr>
          <th class="label">Notation</th>
          <td class="value">
            <ul>
              <li>{{jsonElementData.result.primaryTopic.notation}}</li>
            </ul>
          </td>
        </tr>
        <tr>
          <th class="label">Comments</th>
          <td class="value">
            <ul>
              <li
                v-for="comment in jsonElementData.result.primaryTopic.comment"
                v-bind:key="comment"
              >{{comment._value}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.narrower">
          <th class="label">Interval Contains</th>
          <td class="value">
            <ul>
              <li>
                <table
                  class="nested-table"
                  v-for="child in jsonElementData.result.primaryTopic.narrower"
                  v-bind:key="child"
                >
                  <tr>
                    <th colspan="2">{{child.label._value}}</th>
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
        <tr>
          <th class="label">Interval During</th>
          <td class="value">
            <ul>
              <li>
                <table
                  class="nested-table"
                  v-for="parent in jsonElementData.result.primaryTopic.broader"
                  v-bind:key="parent"
                >
                  <tr>
                    <th colspan="2">{{parent.label._value}}</th>
                  </tr>
                  <tr>
                    <td class="label">Interval Contains</td>
                    <td class="value">{{jsonElementData.result.primaryTopic.label._value}}</td>
                  </tr>
                </table>
              </li>
              <li>
                <table
                  class="nested-table"
                  v-for="parent in jsonElementData.result.primaryTopic.broaderTransitive"
                  v-bind:key="parent"
                >
                  <tr>
                    <th colspan="2">{{parent.label._value}}</th>
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
          <th class="label">Interval Started By</th>
          <td class="value">
            <ul>
              <li>{{jsonElementData.result.primaryTopic.intervalStartedBy.label._value}}</li>
            </ul>
          </td>
        </tr>
        <tr>
          <th class="label">Beginning</th>
          <td class="value">
            <ul>
              <li>{{jsonElementData.result.primaryTopic.hasBeginning.label._value}}</li>
            </ul>
          </td>
        </tr>
        <tr v-if="jsonElementData.result.primaryTopic.intervalFinishedBy != null">
          <th class="label">Interval Finished By</th>
          <td class="value">
            <ul>
              <li>{{jsonElementData.result.primaryTopic.intervalFinishedBy.label._value}}</li>
            </ul>
          </td>
        </tr>
        <tr>
          <th class="label">End</th>
          <td class="value">
            <ul>
              <li>{{jsonElementData.result.primaryTopic.hasEnd.label._value}}</li>
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
    jsonElementData: Array
  }
};
</script>


<style>
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
#datasheet {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
}
#datasheet-overlay {
  overflow: visible;
  position: fixed;
  top: 0;
  height: 100%;
  width: 100%;
  opacity: 0.75;
  background-color: black;
  z-index: 1;
}
#datasheet-container {
  position: fixed;
  overflow: auto;
  background-color: white;
  width: 50%;
  height: 80%;
  margin-top: 5%;
  margin-bottom: 5%;
  left: 25%;
  right: 25%;
  z-index: 2;
  box-shadow: 2px 2px 5px black;
  border: 1px solid black;
  padding: 20px;
  background-color: #e9e9e9;
}
#datasheet-exit-button {
  transition: opacity 0.5s;
  position: fixed;
  top: 0;
  right: 0;
  height: 75px;
  width: 75px;
  padding-top: 0px;
  background-color: black;
  opacity: 0.25;
  border-bottom-left-radius: 95%;
  z-index: 2;
}
#datasheet-exit-button:hover {
  opacity: 0.75;
  transition: opacity 0.5s;
  cursor: pointer;
}
#datasheet-exit-button-text {
  position: fixed;
  font-size: 26px;
  font-weight: bold;
  color: white;
  top: 10px;
  right: 20px;
  z-index: 3;
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
#datasheet-header a:hover,
#datasheet-header a:focus {
  background-size: 100% 2px;
}
#datasheet-container {
  transition: transform 0.2s;
}
#datasheet-container:hover {
  background-color: pink;
  transform: translateX(-100%);
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
table,
td,
th {
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