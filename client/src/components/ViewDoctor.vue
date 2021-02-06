<template>
    <center>
        <div id="wrapper">
            <div id="about">
                <img id="image" width="35%" :src="photo"/>
                <h1>{{ name }}</h1>
                <h2 id="methods_header"> Методы </h2>
                <div id="methods" v-for="method in methods" :key="method">
                    <p>{{ method }}</p>
                </div>
            </div>
        </div>
    </center>
</template>

<style>
#about {
    text-align: left;
}

#about img {
    float: left;
    margin-right: 20px;
}

#image {
    margin: auto;
}

#methods {
    margin-top: -30px;
}

#methods_header {
    margin-top: -10px;
    margin-bottom: 45px;
}

#methods p {
    float: left;
    padding: 5px;
    background: #E8E8E8;
    margin-right: 10px;
    margin-top: -10px;
    padding-left: 10px;
    padding-right: 10px;
}
</style>

<script>
import { findDoctor } from "../helpers/doctors"

export default {
    name: "ViewDoctor",
    computed: {
        name () {
            return findDoctor(this.$store.getters.DOCTORS, this.$route.params.id).name
        },
        methods () {
            return findDoctor(this.$store.getters.DOCTORS, this.$route.params.id).methods
        },
        photo () {
            return findDoctor(this.$store.getters.DOCTORS, this.$route.params.id).photo
        }
    }
}
</script>