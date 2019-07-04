<template>
    <div id="container">
        <svg width="100%" :height="'40px'" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <g class='headings'>
                <text x="7.5%" y="50%">Supereon</text>
                <text x="17.5%" y="50%"><tspan x="17.5%" y="30%">Eonothem /</tspan><tspan x="17.5%" y="70%">Eon</tspan></text>
                <text x="27.5%" y="50%"><tspan x="27.5%" y="30%">Erathem /</tspan><tspan x="27.5%" y="70%">Era</tspan></text>
                <text x="37.5%" y="50%"><tspan x="37.5%" y="30%">System /</tspan><tspan x="37.5%" y="70%">Period</tspan></text>
                <text x="57.5%" y="50%">Series / Epoch</text>
                <text x="86.25%" y="50%">Stage / Age</text>
            </g>
        </svg>
        <svg class="animated-svg" width="100%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <g v-for="item in entries" v-bind:key="item.id" :id="item.id" @click='sendClickToEventBus'>
                <rect  :class="item.type" :fill="item.fill" :width="(parseFloat(item.width) + 2.5) + '%'" :stroke="'black'" :height="item.height" :x="item.x" :y="item.y">
                </rect>
                <text  :class="item.type" :x="item.xlabel" :y="item.ylabel">{{(item.name.slice(-4) == "Null")? "" : item.name }}</text>
            </g>
        </svg>
    </div>
</template>
<script>
    import data from '../assets/timeline_data.json'
    import numericTimeData from '../assets/time_interval_data.json'
    import EventBus from '../assets/event-bus.js'
    export default {
        name: 'graphic',
        methods: {
            sendClickToEventBus: function(event) {
                EventBus.$emit('create-data-sheet', event.target.parentNode.id)
            },
            stretchElement: function(event){
                var target = event.originalTarget.parentNode.childNodes[0]
                var currentWidth = parseFloat(target.getAttribute('width'))
                target.setAttribute('width', (currentWidth + 2.4) + "%")
            },
            unStretchElement: function(event){
                var target = event.originalTarget.parentNode.childNodes[0]
                var currentWidth = parseFloat(target.getAttribute('width'))
                target.setAttribute('width', (currentWidth - 2.4) + "%")
            },
            baseLog: function(x, y){
                return Math.log(y) / Math.log(x)
            },
            preprocessPositionsLogarithmic: function(data, intervalData){
                var base = 50
                var precambrian = false
                var archean = false
                for (let item in data){
                    if (data[item]['id'] == "Precambrian") {// Necessary as precambrian supereon has no epochs
                        precambrian = true
                    } 
                    if (data[item]['id'] == "Archean") {// Necessary as archean eon has no periods
                        archean = true
                    }
                    var end = this.baseLog(base, intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd'] + 1) / this.baseLog(base, 4568) * 100
                    var beginning = this.baseLog(base, intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasBeginning'] + 1) / this.baseLog(base, 4568) * 100
                    data[item]['y'] = (end != -Infinity) ? end + "%" : '0%'
                    data[item]['height'] = (beginning - parseFloat(data[item]['y'])) + '%'
                    data[item]['ylabel'] = (parseFloat(data[item]['y']) +  (parseFloat(data[item]['height'])) /2) + '%'
                    if (data[item]['type'] == 'age'){
                        data[item]['x'] = "72.5%"
                        data[item]['width'] = "27.5%"
                        data[item]['xlabel'] = "86.25%"
                    }else if (data[item]['type'] == 'epoch sub-epoch'){
                        data[item]['x'] = "57.5%"
                        data[item]['width'] = "42.5%"
                        data[item]['xlabel'] = "65%"
                    }else if (data[item]['type'] == 'epoch'){
                        data[item]['x'] = "42.5%"
                        data[item]['width'] = "57.5%"
                        data[item]['xlabel'] = (data[item]['id'] == 'Mississippian' || data[item]['id'] == 'Pennsylvanian') ? "50%" : "57.5%"
                    }else if (data[item]['type'] == 'period'){
                        data[item]['x'] = "32.5%"
                        data[item]['width'] = "67.5%"
                        data[item]['xlabel'] = "37.5%"
                        if (precambrian){
                            data[item]['xlabel'] = "67.5%"
                        }
                    }else if (data[item]['type'] == 'era'){
                        data[item]['x'] = "22.5%"
                        data[item]['width'] = "77.5%"
                        data[item]['xlabel'] =  (!precambrian) ? "27.5%" : "27.5%"
                        if (archean){
                             data[item]['xlabel'] = "62.5%"
                        }
                    }else if (data[item]['type'] == 'eon'){
                        data[item]['x'] = "12.5%"
                        data[item]['width'] = "87.5%"
                        data[item]['xlabel'] = "17.5%"
                        if (data[item]['id'] == 'Hadean'){
                             data[item]['xlabel'] = "56.25%"
                        }
                    }else if (data[item]['type'] == 'super-eon'){
                        data[item]['x'] = "2.5%"
                        data[item]['width'] = "97.5%"
                        data[item]['xlabel'] = "7.5%"
                    }
                }
                return data
            }
        },
        data () {
            return {
                intervalData: numericTimeData,
                dividerPosition: -1,
                entries: this.preprocessPositionsLogarithmic(data, numericTimeData)
            }
        }
    }
</script>
<style scoped>
    #container {
        position: relative;
        border: solid white 1px;
        width: 75%;
        min-width: 980px;
        max-width: 1250px;
        margin: auto;
        height: 30000px;
    }
    svg{
        background-color: white;
        overflow: auto;
    }
    .animated-svg {
        border-right: solid black 1px;
    }
    rect{
        stroke-width: 1;
        stroke: black;
    }
    text{
        dominant-baseline: middle;
        text-anchor: middle;
        font-weight: bold;
    }
    g{
        position: relative;
        right: 0px;
        top: 0px;
        transition: transform .2s ease-in-out;
    }
    .animated-svg g:hover{
        /*transform-origin: 100% 100%;
        transform: scale(1.1, 1);*/ 
        transform: translate3d(-2.4%, 0px, 0px);
        transform-origin: 100% 100%;
        cursor: pointer;
    }
    /*
    .animated-svg g rect{
        transition: all .2s ease-in-out;
    }
    .animated-svg g rect:hover{
        width: 500px;
    }*/
</style>


