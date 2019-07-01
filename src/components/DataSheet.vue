<template>
    <div id='datasheet'>
        <div id='datasheet-overlay' @click='destroyDataSheet'></div>
        <div id="datasheet-exit-button" @click='destroyDataSheet'><div id="datasheet-exit-button-text">&#x2573;</div></div>
        <div id='datasheet-container' v-if="dataReceived">
            <data-sheet-basic v-bind:jsonElementData="jsonElementData"></data-sheet-basic>
        </div>
    </div>
</template>

<script>
import EventBus from "../assets/event-bus.js"
import DataSheetBasic from './DataSheetBasic.vue'
export default {
    name: 'DataSheet',
    components: {
        DataSheetBasic
    },
    props: {
        id: String
    },
    data (){
        return {
            jsonElementData: "Waiting",
            dataReceived: true
        }
    },
    methods: {
        httpRequestAsync: function(url){
            var this_ = this
            var xmlHttp = new XMLHttpRequest()
            xmlHttp.onreadystatechange = function () {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
                    var data = xmlHttp.responseText
                    this_.jsonElementData = JSON.parse(data)
                    this_.dataReceived = true
                    console.log(data)
            }
        }
        xmlHttp.open("GET", url, true)
        xmlHttp.send(null)
        },
        destroyDataSheet: function() {
            EventBus.$emit('destroy-data-sheet', true)
        }
    },
    mounted(){
        var requestURL = 'https://vocabs.ands.org.au/repository/api/lda/csiro/international-chronostratigraphic-chart/2018-revised/resource.json?uri=http://resource.geosciml.org/classifier/ics/ischart/' + this.id
        this.httpRequestAsync(requestURL)
    }
}
</script>


<style>
    p{
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
    #datasheet-overlay{
        overflow: visible;
        position: fixed;
        top: 0;
        height: 100%;
        width: 100%;
        opacity: 0.75;
        background-color: black;
        z-index: 1;
    }
    #datasheet-container{
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
        background-color: #E9E9E9;
    }
    #datasheet-exit-button{
        transition: opacity .5s;
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
    #datasheet-exit-button:hover{
        opacity: 0.75;
        transition: opacity .5s;
        cursor: pointer;
    }
    #datasheet-exit-button-text{
        position: fixed;
        font-size: 26px;
        font-weight: bold;
        color: white;
        top: 10px;
        right: 20px;
        z-index: 3;
    }
    #datasheet-header{
        border: 3px solid lightgray;
        border: 0;
        padding: 10px;
        margin-bottom: 0;
        width: 75%;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
        background-color: #0C415A;
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
        transition: background-size .2s ease-in-out;
    }
    #datasheet-header a:hover, #datasheet-header a:focus {
        background-size: 100% 2px;
    }
    #datasheet-container{
        transition: transform .2s;
    }
    #datasheet-container:hover{
        background-color: pink;
        transform: translateX(-100%);
    }
    #table-container{
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
    table{
        width: 100%;
    }
    td{
        width: 60%;
    }
    td li{
        display: block;
        text-align: left;
    }
    th{
        text-align: left;
        padding-left: 5%;
        padding-top: 16px;
        vertical-align: top;
        padding-right: 5%;
    }
    .nested-table, .nested-table td, .nested-table th {
        border: 1px solid lightgrey;
        border-collapse: collapse;
    }
    .nested-table td{
        font-size: 0.9em;
        text-align: left;
        padding-left: 5%;
        padding-right: 5%;
    }
    .nested-table th{
        background-color: #dae2e6;
    }
    .nested-table .label{
        width: 40%;
    }

</style>