<template>
    <div id="container">
        <!-- 'y' must increase and must be the previous 'y' + previous 'height' -->
        <svg width="100%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <rect class="eon" id="Phanerozoic" fill="#A1D4E2" x="0" y="0" width="100%" height="100%" stroke="black" stroke-width="5"/>
                <rect class="era" id="Cenozoic" fill="#F6EB3B" x="10%" y="0" width="100%" height="16.67%"/>
                <rect class="era" id="Mesozoic" fill="#6CC0DB" x="10%" y="16.67%" width="100%" height="16.67%"/>
                <rect class="era" id="Paleozoic" fill="#A3BC99" x="10%" y="33.33%" width="100%" height="16.67%"/>
                <rect class="era" id="Proterozoic" fill="#EA5B70" x="10%" y="50%" width="100%" height="16.67%"/>
                <rect class="era" id="Archean" fill="#E72582" x="10%" y="66.67%" width="100%" height="16.67%"/>
                <rect class="era" id="Hadean" fill="#B12A7E" x="10%" y="83.34%" width="100%" height="100%"/>
        </svg>

    </div>
</template>
<script>
export default {
    name: 'graphic',

}
</script>
<style scoped>
    #container {
        border: solid black 1px;
        max-width: 75%;
        margin: auto;
        height: 3000px;;
    }
    svg{
        background-color: red;
    }
    rect{
        stroke-width: 1;
        stroke: black;
    }
</style>


