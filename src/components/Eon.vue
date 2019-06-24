<template>
    <div id="eon-container" :style="style">
        <span class='vertical-heading'>{{eonName}}</span>
    </div>
</template>
<script>
    export default {
        name: 'Eon', 
        props: {
            eonName: String,
            color: String
        },
        computed: {
            style() {
                return 'background-color: ' + this.color
            }
        }
    }
</script>
<style scoped>
    #eon-container{
        border: solid black 1px;
    }
    .vertical-heading {
        writing-mode: vertical-rl;
        text-orientation: mixed
    }
</style>
