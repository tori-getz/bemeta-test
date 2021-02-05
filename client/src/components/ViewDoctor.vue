<template>
    <center>
        <div id="wrapper">
            <div id="image-block">
                <img id="image" width="100%" :src="photo"/>
            </div>
            <div id="about">
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
#wrapper {
    width: 55%;
    display: flex;
    flex-direction: fow;
}

#about {
    text-align: left;
    width: 80%;
    float: right;
}

#image-block {
    display: flex;
    flex-direction: colum;
    justify-content: center;
    float: left;
    width: 70%;
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
export default {
    name: "ViewDoctor",
    props: {
        photo: String,
        name: String,
        methods: Array
    }
}
</script>