<template>
<header>
  <div class="wrap">
		<div class="site-title">
      <router-link :to="{ path: '/'}">
      <h1>치킨 그룹</h1>
      <h3>Chicken Group</h3>
      </router-link>
		</div>
		<div class="right-search">
			<input type="" name="" class="right-search-box" v-on:change="search" v-on:keyup="search">
		</div>

		<div class="right-gbn">
			<ul>
				<li class="recruite selected" @click="select('recruite')">
            구인구직
        </li>
        <li class="station" @click="select('station')">
            정거장
        </li>
			</ul>
		</div>
		<div class="left-length">
			총 개수 : {{listTotalLength}}
		</div>
	</div>
</header>
</template>

<script>
import { eventBus } from '../main.js';

export default {
  name: 'main-header',
	methods: {
    search: function (event) {
			let value = event.target.value;
			let pattern = new RegExp('.*' + value + '.*');
			let list = this.$parent.$el.querySelectorAll('.container');

			list.forEach(element => {
				if(pattern.test(element.querySelector('.item-title').textContent)) {
					element.style.display = "inline-block";
				} else {
					element.style.display = "none";
				}
			});
    },
    select (menu){
      let menuBtn = document.querySelector('.'+menu)
      let recCnt = document.querySelector('.left-length')
      let search = document.querySelector('.right-search')
      menuBtn.classList.add('selected')
      if (menu=='recruite'){
        let stationBtn = document.querySelector('.station')
        stationBtn.classList.remove('selected')
        recCnt.style.display = "inline-block"
        search.style.display = "inline-block"
        this.$router.push({name: menu})
      } else {
        let recruiteBtn = document.querySelector('.recruite')
        recruiteBtn.classList.remove('selected')
        recCnt.style.display = "none"
        search.style.display = "none"
        this.$router.push({name: menu})
      }
      return
    }
	},
	data: function() {
	return {
			listTotalLength: 0
		}
	},
	created() {
		eventBus.$on('listChange', (length) => {
			this.listTotalLength = length;
		});
	}
}


</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
