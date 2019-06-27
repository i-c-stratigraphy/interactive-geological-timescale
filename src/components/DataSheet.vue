<template>
    <div id='datasheet'>
        <div id='datasheet-overlay' @click='destroyDataSheet'></div>
        <div id="datasheet-exit-button" @click='destroyDataSheet'><div id="datasheet-exit-button-text">&#x2573;</div></div>
        <div id='datasheet-container'>
            <p>ID: {{id}}</p>
            <p v-if="dataReceived">DATA: {{elementData}}</p>
        </div>
    </div>
</template>

<script>
import EventBus from "../assets/event-bus.js"
export default {
    name: 'DataSheet',
    props: {
        id: String
    },
    data (){
        return {
            elementData: "Waiting",
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
                    this_.elementData = data
                    this_.dataReceived = true
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
        var requestURL = 'http://vocabs.ands.org.au/repository/api/lda/csiro/international-chronostratigraphic-chart/2018-revised/resource.json?uri=http://resource.geosciml.org/classifier/ics/ischart/' + this.id
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

</style>