<template>
    <div id="app">
    <h1>회사들 목록</h1>
        <ul>
            <li v-for="i in items" :key="i.id">
                <v-app>
                <v-layout>
                        <v-card>
                            <v-img class="blue--text" :src="img_src" height="150px">
                                <v-container>
                                    <v-layout >
                                        <v-flex>
                                            <span class="headline">{{ i.title }}</span>
                                        </v-flex>
                                    </v-layout>
                                </v-container>
                            </v-img>
                            <v-card-title>
                                <div>
                                    <span>{{ i.id }}</span><br>
                                    <span>{{ i.title }}</span><br>
                                    <span>{{ i.content }}</span>
                                </div>
                            </v-card-title>
                            <v-card-actions>
                                <v-btn text color="orange">공유</v-btn>
                                <v-btn text color="red">더 보기</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-layout>
                </v-app>
            </li>
        </ul>
    </div>
</template>
<style>
ul {
    list-style:none;
    margin:0;
    padding:0;
}
li {
    margin: 0 0 0 0;
    padding: 0 0 0 0;
    border : 0;
    float: left;
    padding-top: 4%;
    padding-left: 4%;
    max-width: 300px;
}
.application--wrap {
    min-height:10vh !important;
}
</style>
