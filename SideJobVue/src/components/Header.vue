<template>
<header>
  <div class="wrap">
		<div class="right-search">
			<input type="" name="" class="right-search-box" v-on:change="search" v-on:keyup="search">
		</div>

		<div class="right-gbn">
			<ul>
				<li class="selected">
					정거장
				</li>
				<li>
					구인구직
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
