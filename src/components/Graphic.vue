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
                <text  :class="item.type" :x="item.xlabel" :y="(parseFloat(item.y) +  parseFloat(item.height) /2) + '%'">{{(item.name.slice(-4) == "Null")? "" : item.name }}</text>
            </g>
        </svg>
    </div>
</template>
<script>
    import data from '../assets/timeline_data.json'
    import EventBus from '../assets/event-bus.js'
    
    export default {
        name: 'graphic',
        methods: {
            calculateAgeHeight: function (data){
                var counter = 0
                var precambrian = false
                var archean = false
                for (let item in data){
                    if (data[item]['id'] == "Precambrian"){
                        precambrian = true
                    } else if (data[item]['id'] == "Archean"){
                        archean = true
                    }
                    if (!precambrian && data[item]['type'] == 'age'){
                        counter++
                    } else if ((precambrian && data[item]['type'] == 'period') || (archean && data[item]['type'] == 'era')){
                        counter++
                        counter++
                    }
                }
                return 100/(counter + 5) // '+ 5' is to correct issues by the Hadean Era not having any associated ages, but still needing to take up space.
            },
            sendClickToEventBus: function(event) {
                EventBus.$emit('create-data-sheet', event.target.parentNode.id)
            },
            stretchElement: function(event){
                console.log(event.originalTarget.parentNode.id)

                var target = event.originalTarget.parentNode.childNodes[0]
                var currentWidth = parseFloat(target.getAttribute('width'))
                target.setAttribute('width', (currentWidth + 2.4) + "%")
            },
            unStretchElement: function(event){
                var target = event.originalTarget.parentNode.childNodes[0]
                var currentWidth = parseFloat(target.getAttribute('width'))
                target.setAttribute('width', (currentWidth - 2.4) + "%")
            },
            preprocessPositions: function(data, ageHeight){
                var yPositionAge = 0
                var toUpdateHeight = []
                var lastSuperEon, lastEon, lastEra, lastPeriod, pastType
                const elementOrder = { 
                    'super-eon':0,
                    'eon': 1, 
                    'era': 2, 
                    'period': 3, 
                    'epoch': 4, 
                    'epoch sub-epoch': 5, 
                    'age': 6
                }
                var precambrian = false
                var archean = false
                for (let item in data){
                    if (data[item]['type'] != [pastType] && elementOrder[data[item]['type']] < elementOrder[pastType]){
                        if (data[item]['type'] == 'period'){
                            toUpdateHeight.push([lastPeriod, (yPositionAge - parseFloat(data[lastPeriod]['y'])) + '%'])
                        } else if (data[item]['type'] == 'era'){
                            if (!precambrian) toUpdateHeight.push([lastPeriod, (yPositionAge - parseFloat(data[lastPeriod]['y'])) + '%'])
                            toUpdateHeight.push([lastEra, (yPositionAge - parseFloat(data[lastEra]['y'])) + '%'])
                        } else if (data[item]['type'] == 'eon'){
                            if (!precambrian) toUpdateHeight.push([lastPeriod, (yPositionAge - parseFloat(data[lastPeriod]['y'])) + '%'])
                            toUpdateHeight.push([lastEra, (yPositionAge - parseFloat(data[lastEra]['y'])) + '%'])
                            toUpdateHeight.push([lastEon, (yPositionAge - parseFloat(data[lastEon]['y'])) + '%'])
                        }else if (data[item]['type'] == 'super-eon'){
                            if (!precambrian) toUpdateHeight.push([lastPeriod, (yPositionAge - parseFloat(data[lastPeriod]['y'])) + '%'])
                            toUpdateHeight.push([lastEra, (yPositionAge - parseFloat(data[lastEra]['y'])) + '%'])
                            toUpdateHeight.push([lastEon, (yPositionAge - parseFloat(data[lastEon]['y'])) + '%'])
                        }
                    }
                    if (data[item]['id'] == "Precambrian") {// HATE this, but necessary as precambrian eon has no periods
                        precambrian = true
                    } 
                    if (data[item]['id'] == "Archean") {// HATE this, but necessary as precambrian eon has no periods
                        archean = true
                    } 
                    if (data[item]['type'] == 'age'){
                        data[item]['x'] = "72.5%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['height'] = ageHeight + '%'
                        data[item]['width'] = "27.5%"
                        data[item]['xlabel'] = "86.25%"
                        yPositionAge = yPositionAge + ageHeight
                    }else if (data[item]['type'] == 'epoch sub-epoch'){
                        data[item]['x'] = "57.5%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['height'] = ageHeight * data[item]['narrow'].length + '%'
                        data[item]['width'] = "42.5%"
                        data[item]['xlabel'] = "65%"
                    }else if (data[item]['type'] == 'epoch'){
                        data[item]['x'] = "42.5%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['height'] = ageHeight * data[item]['narrow'].length + '%'
                        data[item]['width'] = "57.5%"
                        data[item]['xlabel'] = (data[item]['id'] == 'Mississippian' || data[item]['id'] == 'Pennsylvanian') ? "50%" : "57.5%"
                    }else if (data[item]['type'] == 'period'){
                        lastPeriod = item
                        data[item]['x'] = "32.5%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['width'] = "67.5%"
                        data[item]['xlabel'] = "37.5%"
                        if (precambrian){
                            data[item]['height'] = ageHeight*2 + '%'
                            yPositionAge = yPositionAge + ageHeight*2
                            data[item]['xlabel'] = "67.5%"
                        }
                    }else if (data[item]['type'] == 'era'){
                        lastEra = item
                        data[item]['x'] = "22.5%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['width'] = "77.5%"
                        data[item]['xlabel'] =  (!precambrian) ? "27.5%" : "27.5%"
                        if (archean){
                            data[item]['height'] = ageHeight*2 + '%'
                            yPositionAge = yPositionAge + ageHeight*2
                            data[item]['xlabel'] = "62.5%"
                        }
                    }else if (data[item]['type'] == 'eon'){
                        lastEon = item
                        data[item]['x'] = "12.5%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['width'] = "87.5%"
                        data[item]['xlabel'] = "17.5%"
                        // Making Hadean Eon the Height of 5 Ages
                        if (precambrian && data[item]['id'] == 'Hadean') {
                            data[item]['height'] = ageHeight * 5 + "%"
                            yPositionAge = yPositionAge + (ageHeight * 5)
                            data[item]['xlabel'] =  "57.5%"
                        }
                    }else if (data[item]['type'] == 'super-eon'){
                        lastSuperEon = item
                        data[item]['x'] = "2.5%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['width'] = "97.5%"
                        data[item]['xlabel'] = "7.5%"
                    }
                    pastType = data[item]['type']
                    if (item == data.length - 1){
                        toUpdateHeight.push([lastSuperEon, (yPositionAge - parseFloat(data[lastSuperEon]['y'])) + '%'])
                    }
                    /*
                    if (precambrian && data[item]['type'] != 'age' && data[item]['type'] == [pastType]){
                        toUpdateHeight.push([item, ageHeight + "%"])
                        yPositionAge = yPositionAge + ageHeight
                    }
                    */

                }
                for (let item in toUpdateHeight){
                    data[toUpdateHeight[item][0]]['height'] = toUpdateHeight[item][1]
                    
                }
                return data
            }
        },
        data () {
            return {
                dividerPosition: -1,
                ageHeight: this.calculateAgeHeight(data),
                entries: this.preprocessPositions(data, this.calculateAgeHeight(data))
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
        height: 3500px;
    }
    svg{
        background-color: white;
        overflow: auto;
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
    }
    g {
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


