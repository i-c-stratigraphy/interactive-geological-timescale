<template>
    <div id="header">
        <h1><span id="smaller-heading">INTERACTIVE</span><br>INTERNATIONAL CHRONOSTRATIGRAPHIC CHART</h1>
        <p>An interactive version of the <a href="http://www.stratigraphy.org/index.php/ics-chart-timescale">International Chronostratigraphic Chart</a>, based on its <a href="https://www.w3.org/standards/semanticweb/">Semantic Web</a> representation.</p>
        <p>For comments/issues and this visualisation's code, please see its <a href="https://github.com/CSIRO-enviro-informatics/interactive-geological-timescale">Git Code Repository</a>.</p><br>
    </div>
</template>

<script>
export default {
  name: 'Heading'
}
</script>


<style scoped>
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
    #smaller-heading{
        font-size: 0.8em;
    }
</style>
