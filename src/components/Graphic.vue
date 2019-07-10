<template>
    <transition name="fade">
    <div id="container" :style="'height: ' + containerHeight + 'px;'" v-if="loaded">
        <br>
        <svg class='headings' width="95%" :height="'40px'" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <g>
                <text x="7.5%" y="50%">Supereon</text>
                <text x="17.5%" y="50%"><tspan x="17.5%" y="30%">Eonothem /</tspan><tspan x="17.5%" y="70%">Eon</tspan></text>
                <text x="27.5%" y="50%"><tspan x="27.5%" y="30%">Erathem /</tspan><tspan x="27.5%" y="70%">Era</tspan></text>
                <text x="37.5%" y="50%"><tspan x="37.5%" y="30%">System /</tspan><tspan x="37.5%" y="70%">Period</tspan></text>
                <text x="57.5%" y="50%">Series / Epoch</text>
                <text x="86.25%" y="50%">Stage / Age</text>
            </g>
        </svg>
        <svg class="animated-svg" width="95%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <g v-for="item in entries" v-bind:key="item.id" :id="item.id" @click='sendClickToEventBus'> 
                    <rect  :class="item.type" :fill="item.fill" :width="(parseFloat(item.width) + 2.5) + '%'" :stroke="'black'" :height="item.height" :x="item.x" :y="item.y">
                    </rect>
                    <text v-if="parseFloat(item.height) >= threshold" :ref="item.id" :class="item.type" :x="item.xlabel" :y="item.ylabel">{{(item.name.slice(-4) == "Null")? "" : item.name }}</text>
                    <title v-else>{{(item.name.slice(-4) == "Null")? "" : item.name }}</title>

            </g>
        </svg>
        <svg class="timescale-label" width="5%" height="40px" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <text x="50%" y="50%"><tspan x='50%' y='30%'>Numerical</tspan><tspan x='50%' y='70%'>Age (Ma)</tspan></text>
        </svg>
        <svg class="timescale" width="5%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <g v-for="(item, index) in entries" v-if="intervalChildrenData['http://resource.geosciml.org/classifier/ics/ischart/' + item.id] == 0 && parseFloat(item.height) >= threshold" v-bind:key="index">
                <line x1="0" :y1="item.y" x2="30%" :y2="item.y" stroke='black'/>
                <text :x="'30%'" :y="item.y">{{intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + item.id].hasEnd}}</text>
            </g>
            <g>
                <text x='25%' y="100%">~4600</text>
            </g>
        </svg>
    </div>
    <div id='loading-icon' v-else>
        <img src="../assets/loading.svg" width="120px" height="120px">
        <p>Loading...</p>
    </div>
    </transition>
</template>
<script>
    import data from '../assets/timeline_data.json'
    import numericTimeData from '../assets/time_interval_data.json'
    import intervalChildrenData from '../assets/time_interval_children.json'
    import EventBus from '../assets/event-bus.js'
    export default {
        name: 'graphic',
        props: {
            scaleMode: {
                type: String,
                default: 'None'
            },
            containerHeight: {
                type: Number,
                default: 3500

            }
        },
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
            },
            preprocessPositionsLinear: function(data, intervalData){
                var total = 4567
                var precambrian = false
                var archean = false
                for (let item in data){
                    if (data[item]['id'] == "Precambrian") {// Necessary as precambrian supereon has no epochs
                        precambrian = true
                    } 
                    if (data[item]['id'] == "Archean") {// Necessary as archean eon has no periods
                        archean = true
                    }
                    var end = (intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd']) / total * 100
                    var beginning = (intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasBeginning']) / total * 100
                    data[item]['y'] = end + "%"
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
            },
            countChildlessChildren: function(id, intervalChildrenData){
                var counter = 0
                if (intervalChildrenData[id].length == 0){
                    return 0
                } else{
                    for (let child in intervalChildrenData[id]){
                        if (intervalChildrenData[intervalChildrenData[id][child]].length == 0){
                            counter ++
                        }
                    }
                    return counter
                }
            },
            preprocessChildData: function(){
                var countArray = {}
                for (let id in this.intervalChildrenData){
                    countArray[id] = this.countChildlessChildren(id, this.intervalChildrenData)
                }
                return countArray
            },
            preprocessPositionsNoscale: function(data, intervalData, intervalChildrenData){
                var precambrian = false
                var archean = false
                var ageBlocks = 0
                var ages = [], epochs = [], subEpochs = [], periods = [], eras = [], eons = [], supereons = []
                var currentAgeY = 0, currentEpochY = 0, currentSubEpochY = 0, currentPeriodY = 0, currentEraY = 0, currentEonY = 0, currentSupereonY = 0
                for (let item in intervalChildrenData){
                    if (intervalChildrenData[item] == 0){
                        ageBlocks ++
                    }
                }
                var blockHeight = 100 / (ageBlocks - 1)
                for (let item in data){
                    if (data[item]['id'] == "Precambrian") {// Necessary as precambrian supereon has no epochs
                        precambrian = true
                    } 
                    if (data[item]['id'] == "Archean") {// Necessary as archean eon has no periods
                        archean = true
                    }
                    if (data[item]['type'] == 'age'){
                        ages.push([data[item]['id'], intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd']])
                        data[item]['x'] = "72.5%"
                        data[item]['width'] = "27.5%"
                        data[item]['xlabel'] = "86.25%"
                    }else if (data[item]['type'] == 'epoch sub-epoch'){
                        subEpochs.push([data[item]['id'], intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd']])
                        data[item]['x'] = "57.5%"
                        data[item]['width'] = "42.5%"
                        data[item]['xlabel'] = "65%"
                    }else if (data[item]['type'] == 'epoch'){
                        epochs.push([data[item]['id'], intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd']])
                        data[item]['x'] = "42.5%"
                        data[item]['width'] = "57.5%"
                        data[item]['xlabel'] = (data[item]['id'] == 'Mississippian' || data[item]['id'] == 'Pennsylvanian') ? "50%" : "57.5%"
                    }else if (data[item]['type'] == 'period'){
                        periods.push([data[item]['id'], intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd']])
                        data[item]['x'] = "32.5%"
                        data[item]['width'] = "67.5%"
                        data[item]['xlabel'] = "37.5%"
                        if (precambrian){
                            data[item]['xlabel'] = "67.5%"
                        }
                    }else if (data[item]['type'] == 'era'){
                        eras.push([data[item]['id'], intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd']])
                        data[item]['x'] = "22.5%"
                        data[item]['width'] = "77.5%"
                        data[item]['xlabel'] =  (!precambrian) ? "27.5%" : "27.5%"
                        if (archean){
                             data[item]['xlabel'] = "62.5%"
                        }
                    }else if (data[item]['type'] == 'eon'){
                        eons.push([data[item]['id'], intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd']])
                        data[item]['x'] = "12.5%"
                        data[item]['width'] = "87.5%"
                        data[item]['xlabel'] = "17.5%"
                        if (data[item]['id'] == 'Hadean'){
                             data[item]['xlabel'] = "56.25%"
                        }
                    }else if (data[item]['type'] == 'super-eon'){
                        supereons.push([data[item]['id'], intervalData['http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']]['hasEnd']])
                        data[item]['x'] = "2.5%"
                        data[item]['width'] = "97.5%"
                        data[item]['xlabel'] = "7.5%"
                    }
                }
                ages.sort(function(a,b) {
                    return a[1] - b[1]
                })
                epochs.sort(function(a,b) {
                    return a[1] - b[1]
                })
                subEpochs.sort(function(a,b) {
                    return a[1] - b[1]
                })
                periods.sort(function(a,b) {
                    return a[1] - b[1]
                })
                eras.sort(function(a,b) {
                    return a[1] - b[1]
                })
                eons.sort(function(a,b) {
                    return a[1] - b[1]
                })
                supereons.sort(function(a,b) {
                    return a[1] - b[1]
                })
                for (let age in ages){
                    let id = 'http://resource.geosciml.org/classifier/ics/ischart/' + ages[age][0]
                    intervalData[id]['y'] = currentAgeY + '%'
                    intervalData[id]['height'] = blockHeight + '%'
                    currentAgeY = parseFloat(intervalData[id]['y']) + parseFloat(intervalData[id]['height'])
                }
                for (let epoch in epochs){
                    let id = 'http://resource.geosciml.org/classifier/ics/ischart/' + epochs[epoch][0]
                    intervalData[id]['y'] = currentEpochY + '%'
                    intervalData[id]['height'] = (intervalChildrenData[id] != 0 ) ? blockHeight * intervalChildrenData[id] + '%' : blockHeight + '%'
                    currentEpochY = parseFloat(intervalData[id]['y']) + parseFloat(intervalData[id]['height'])
                }
                currentSubEpochY = parseFloat(intervalData['http://resource.geosciml.org/classifier/ics/ischart/Pennsylvanian']['y'])// REQUIRED as the two epochs that contain sub-epochs are the Pennsylvanian and Mississippiann Epochs (which are back to back). Hence the y positions of ALL the subperiods start when the Pennsylvanian Epoch starts.
                for (let epoch in subEpochs){
                    let id = 'http://resource.geosciml.org/classifier/ics/ischart/' + subEpochs[epoch][0]
                    intervalData[id]['y'] = currentSubEpochY + '%'
                    intervalData[id]['height'] = (intervalChildrenData[id] != 0 ) ? blockHeight * intervalChildrenData[id] + '%' : blockHeight + '%'
                    currentSubEpochY = parseFloat(intervalData[id]['y']) + parseFloat(intervalData[id]['height'])
                }
                for (let period in periods){
                    let id = 'http://resource.geosciml.org/classifier/ics/ischart/' + periods[period][0]
                    intervalData[id]['y'] = currentPeriodY + '%'
                    intervalData[id]['height'] = (intervalChildrenData[id] != 0 ) ? blockHeight * intervalChildrenData[id] + '%' : blockHeight + '%'
                    currentPeriodY = parseFloat(intervalData[id]['y']) + parseFloat(intervalData[id]['height'])
                }
                for (let era in eras){
                    let id = 'http://resource.geosciml.org/classifier/ics/ischart/' + eras[era][0]
                    intervalData[id]['y'] = currentEraY + '%'
                    intervalData[id]['height'] = (intervalChildrenData[id] != 0 ) ? blockHeight * intervalChildrenData[id] + '%' : blockHeight + '%'
                    currentEraY = parseFloat(intervalData[id]['y']) + parseFloat(intervalData[id]['height'])
                }
                for (let eon in eons){
                    let id = 'http://resource.geosciml.org/classifier/ics/ischart/' + eons[eon][0]
                    intervalData[id]['y'] = currentEonY + '%'
                    intervalData[id]['height'] = (intervalChildrenData[id] != 0 ) ? blockHeight * intervalChildrenData[id] + '%' : blockHeight + '%'
                    currentEonY = parseFloat(intervalData[id]['y']) + parseFloat(intervalData[id]['height'])
                }
                currentSupereonY = currentAgeY // REQUIRED as the precambrian (latest) supereon starts after the Phanerozoic Eon (which has no supereon parent) - this is where ages end.
                for (let supereon in supereons){
                    let id = 'http://resource.geosciml.org/classifier/ics/ischart/' + supereons[supereon][0]
                    intervalData[id]['y'] = currentSupereonY + '%'
                    intervalData[id]['height'] = (intervalChildrenData[id] != 0 ) ? blockHeight * intervalChildrenData[id] + '%' : blockHeight + '%'
                    currentEraY = parseFloat(intervalData[id]['y']) + parseFloat(intervalData[id]['height'])
                }
                for (let item in data){
                    let id = 'http://resource.geosciml.org/classifier/ics/ischart/' + data[item]['id']
                    data[item]['y'] = intervalData[id]['y']
                    data[item]['height'] = intervalData[id]['height']
                    data[item]['ylabel'] = (parseFloat(data[item]['y']) +  (parseFloat(data[item]['height'])) /2) + '%'
                }
                return data
            }
        },
        created() {
            this.loaded = false
            this.intervalChildrenData = this.preprocessChildData()
            if (this.scaleMode == "Logarithmic"){
                this.entries = this.preprocessPositionsLogarithmic(data, this.intervalData)
            } else if (this.scaleMode == "Linear"){
                this.entries = this.preprocessPositionsLinear(data, this.intervalData)
            } else if (this.scaleMode == "None"){
                this.entries = this.preprocessPositionsNoscale(data, this.intervalData, this.intervalChildrenData)
            }
            this.loaded = true
        },
        mounted() {
            // Used to manually wrap labels if necessary. Key in requiredOverride is the original ref of the label (ID in the vocab) and the value is the hyphenated text. Newline is created at the hyphen. NOTE: can only have 1 hyphen
            var requiredOverride = {
                'Neoproterozoic' : 'Neo-proterozoic', 
                'Mesoproterozoic' : 'Meso-proterozoic', 
                'Paleoproterozoic' : 'Paleo-proterozoic'
            }
            var labels = this.$refs
            for (var label in labels){
                if (requiredOverride[label] != null){
                    var object = labels[label][0]
                    var objectX = object.x.baseVal[0].valueInSpecifiedUnits
                    var objectHeight = object.getBBox().height // THIS SOMEHOW CHANGES THE OBJECT THAT THE NEXT COMMAND GETS FROM - FIREFOX
                    var objectY = object.y.baseVal[0].value
                    var newHTML = ''
                    var parsedLabel = requiredOverride[label].split('-')
                    for (let line in parsedLabel){
                        if (line != parsedLabel.length - 1){
                            newHTML += '<tspan x="' + objectX + '%" y="' + (objectY - objectHeight/2) +'">'+ parsedLabel[line] +'-</tspan>'
                        } else {
                            newHTML += '<tspan x="' + objectX + '%" y="' + (objectY + objectHeight/2) +'">'+ parsedLabel[line] +'</tspan>'
                        }
                    }
                    object.innerHTML = newHTML
                }
            }
            
        },
        data() {
            return {
                intervalChildrenData: intervalChildrenData,
                intervalData: numericTimeData,
                dividerPosition: -1,
                entries: null,
                loaded: false,
                threshold: 16/this.containerHeight * 100
            }
        }
    }
</script>
<style scoped>
    #container {
        position: relative;
        border: solid white 1px;
        width: 75%;
        min-width: 1128px;
        max-width: 1250px;
        margin: auto;
    }
    #loading-icon {
        position: relative;
        border: solid white 1px;
        width: 75%;
        min-width: 980px;
        max-width: 1250px;
        margin: auto;
        padding: 50px;
    }
    .headings{
        position: absolute;
        left: 0px;
        top: 0px;
        background-color: white;
    }
    .headings text {
        text-anchor: middle;
        font-weight: bold;
    }
    .timescale-label{
        position: absolute;
        overflow: visible;
        right: 0px;
        left: 95%;
        top: 0px;
        text-anchor: middle;
        font-weight: bold;
        background-color: white;
    }
    .timescale{
        position: absolute;
        overflow: visible;
        right: 0px;
        left: 95%;
        top: 40px;
    }
    .timescale text{
        font-weight: bold;
        dominant-baseline: middle;
    }
    .animated-svg {
        position: absolute;
        border-right: solid black 1px;
        background: repeating-linear-gradient(
            -45deg,
            #F0F0F0,
            #F0F0F0 40px,
            #F2F2F2 40px,
            #F2F2F2 80px
        );
        left:0px;
        top:40px;
        bottom: 0px;
    }
    .animated-svg rect{
        stroke-width: 1;
        stroke: black;
    }
    .animated-svg text{
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
        transform: translate3d(-2.4%, 0px, 0px);
        transform-origin: 100% 100%;
        cursor: pointer;
    }

</style>


