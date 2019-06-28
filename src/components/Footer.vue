<template>
    <div id="foot">
        <br>
        <p><strong>Interactive Geological Timescale</strong></p>
        <p>This visualisation of the <a href="http://www.stratigraphy.org/">International Commission on Stratigraphy</a>'s <a href="http://www.stratigraphy.org/index.php/ics-chart-timescale">Chronostratigraphic Chart</a> uses the <a href="https://www.w3.org/TR/skos-primer/">SKOS</a> &amp; <a href="https://www.w3.org/TR/owl-time/">Time Ontology in OWL</a> representation of it as the <a href="http://resource.geosciml.org/vocabulary/timescale/gts2018">Geological Timescale (2018)</a> for its data.</p>
        <p>The work to develop this was supported by <a href="https://www.csiro.au/">CSIRO</a>'s <a href='https://research.csiro.au/ei/'> Environmental Informatics Group</a> and the <a href='https://www.business.qld.gov.au/industries/mining-energy-water/resources/geoscience-information/gsq'>Geological survey of Queensland</a>.</p>
        <div id="logos">
            <img src="assets/CSIRO_Logo.svg" height="170px"> <img src="assetsGSQ_Logo.jpg" height="170px">
        </div>
        <p>This tool was developed by <a href="https://github.com/JakeJones161096">Jake Hashim-Jones</a>.</p>
    </div>
</template>

<script>
export default {
  name: 'CustomFooter'
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
    #foot{
        position: relative;
        top: 50px;
        padding-bottom: 20px;
        width: 75%;
        min-width: 980px;
        max-width: 1250px;
        margin: auto;
        
    }
</style>