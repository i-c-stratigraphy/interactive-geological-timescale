<template>
    <div id="container">
        <svg width="100%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <g v-for="item in entries" v-bind:key="item.id" :id="item.id" @click='getAdditionalInfo'>
                <rect  :class="item.type" :fill="item.fill" :width="item.width" :stroke="'black'" :height="item.height" :x="item.x" :y="item.y"/>
                <text  :class="item.type" :x="item.xlabel" :y="(parseFloat(item.y) +  parseFloat(item.height) /2) + '%'">{{(item.name.slice(-4) == "Null")? "" : item.name }}</text>
            </g>
        </svg>
    </div>
</template>
<script>
    import data from '../assets/timeline_data.json'
    import EventBus from '../assets/event-bus.js'
    
    //console.log(data)
    export default {
        name: 'graphic',
        methods: {
            calculateAgeHeight: function (data){
                var counter = 0
                for (let item in data){
                    if (data[item]['type'] == 'age'){
                        counter++
                    }
                }
                return 100/(counter + 5) // '+ 5' is to correct issues by the Hadean Era not having any associated ages, but still needing to take up space.
            },
            getAdditionalInfo: function(event) {
                console.log(event.target.parentNode.id)
                console.log(EventBus)
                EventBus.$emit('create-data-sheet', event.target.parentNode.id)
            },
            preprocessPositions: function(data, ageHeight){
                var yPositionAge = 0
                var toUpdateHeight = []
                var lastEon, lastEra, lastPeriod, pastType
                const elementOrder = { 
                    'eon': 0, 
                    'era': 1, 
                    'period': 2, 
                    'epoch': 3, 
                    'epoch sub-epoch': 4, 
                    'age': 5
                }
                var precambrian = false
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
                        }
                    }
                    if (data[item]['id'] == "Precambrian") precambrian = true // HATE this, but necessary as precambrian eon has no periods
                    if (data[item]['type'] == 'age'){
                        data[item]['x'] = "60%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['height'] = ageHeight + '%'
                        data[item]['width'] = "40%"
                        data[item]['xlabel'] = "80%"
                        yPositionAge = yPositionAge + ageHeight
                    }else if (data[item]['type'] == 'epoch sub-epoch'){
                        data[item]['x'] = "45%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['height'] = ageHeight * data[item]['narrow'].length + '%'
                        data[item]['width'] = "55%"
                        data[item]['xlabel'] = "52.5%"
                    }else if (data[item]['type'] == 'epoch'){
                        data[item]['x'] = "30%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['height'] = ageHeight * data[item]['narrow'].length + '%'
                        data[item]['width'] = "70%"
                        data[item]['xlabel'] = (data[item]['id'] == 'Mississippian' || data[item]['id'] == 'Pennsylvanian') ? "37.5%" : "45%"
                    }else if (data[item]['type'] == 'period'){
                        lastPeriod = item
                        data[item]['x'] = "20%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['width'] = "80%"
                        data[item]['xlabel'] = "25%"
                    }else if (data[item]['type'] == 'era'){
                        lastEra = item
                        data[item]['x'] = "10%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['width'] = "90%"
                        data[item]['xlabel'] =  (!precambrian) ? "15%" : "20%"
                        // Making Hadean Era the Width of 5 Ages
                        if (precambrian && data[item]['id'] == 'Hadean') {
                            data[item]['height'] = ageHeight * 5 + "%"
                            yPositionAge = yPositionAge + (ageHeight * 5)
                            data[item]['xlabel'] =  "55%"
                        }
                    }else if (data[item]['type'] == 'eon'){
                        lastEon = item
                        data[item]['x'] = "0%"
                        data[item]['y'] = yPositionAge + '%'
                        data[item]['width'] = "100%"
                        data[item]['xlabel'] = "5%"
                    }
                    pastType = data[item]['type']
                    if (item == data.length - 1){
                        toUpdateHeight.push([lastEon, (yPositionAge - parseFloat(data[lastEon]['y'])) + '%'])
                    }
                }
                for (let item in toUpdateHeight){
                    data[toUpdateHeight[item][0]]['height'] = toUpdateHeight[item][1]
                    
                }
                return data
            }
        },
        data () {
            return {
                ageHeight: this.calculateAgeHeight(data),
                entries: this.preprocessPositions(data, this.calculateAgeHeight(data))
            }
        }
    }
</script>
<style scoped>
    #container {
        border: solid white 1px;
        width: 75%;
        min-width: 980px;
        max-width: 1250px;
        margin: auto;
        height: 3000px;;
    }
    svg{
        background-color: white;
        overflow: visible;
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
        top: 0px;
        transition: transform .2s ease-in-out;
    }
    g:hover{
        transform: translate3d(-2.4%, 0px, 0px);
    }
</style>


