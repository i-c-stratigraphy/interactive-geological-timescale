<template>
    <div id='datasheet-container'>
        Hello World
    </div>
</template>

<script>


export default {
  name: 'DataSheet',
  props: {
      id: String
  },
  mounted() {
      var requestURL = 'http://resource.geosciml.org/classifier/ics/ischart/' + this.id
      console.log(requestURL)
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