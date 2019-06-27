<template>
    <div id='datasheet-container'>
        <p>ID: {{id}}</p>
        <p v-if="dataReceived" @click="show">DATA: {{elementData}}</p>
    </div>
</template>

<script>


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
        show: function(){
            console.log(this.elementData)
        },
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
        }
    },
    mounted(){
        var requestURL = 'http://vocabs.ands.org.au/repository/api/lda/csiro/international-chronostratigraphic-chart/2018-revised/resource.json?uri=http://resource.geosciml.org/classifier/ics/ischart/' + this.id
        this.httpRequestAsync(requestURL)
    }
}
</script>


<style scoped>
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
</style>