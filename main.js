// {
//   "organization": ["ABC Corp"],
//   "appContainers": ["springboot", "vue", "mongo"],
//   "testLibraries": ["junit", "jest"]
// }

var diagramData;

axios.get('example1.json')
.then(function (response) {
	diagramData = response.ada
	console.log(diagramData);
})
.catch(function (error) {
	console.log(error);
});


Vue.component('foundation-tag', {
	props: ['struct'],
	template: '<div class="foundations">{{ struct }}</div>'
})

var foundations = new Vue({
	el: '#foundations-app',
	data: {
		list: []
	},
	mounted(){
		var vueScope = this;
		axios.get('example1.json')
		.then(function (response) {
			vueScope.list = response.data.hosting;
		})
		.catch(function (error) {
			console.log(error);
		});
	}
})


Vue.component('environment-tag', {
	props: ['floor-struct', 'container-struct'],
	template: '<div class="floors">{{ floor-struct }} <container-tag v-bind:struct="container-struct>" </div>'
	components: {
		'containers' : appContainers
	}
})


var environment = new Vue({
	el: '#environment-app',
	data: {
		list: []
	},
	mounted(){
		var vueScope = this;
		axios.get('example1.json')
		.then(function (response) {
			vueScope.list = response.data.environments;
		})
		.catch(function (error) {
			console.log(error);
		});
	}
})

Vue.component('collaboration-tag', {
	props: ['struct'],
	template: '<div class="collaboration">{{ struct }}</div>'
})

var collaboration = new Vue({
	el: '#collaboration-app',
	data: {
		list: []
	},
	mounted(){
		var vueScope = this;
		axios.get('example1.json')
		.then(function (response) {
			vueScope.list = response.data.collaborationTools;
		})
		.catch(function (error) {
			console.log(error);
		});
	}
})

Vue.component('source-tag', {
	props: ['struct'],
	template: '<div class="source">{{ struct }}</div>'
})

var source = new Vue({
	el: '#source-app',
	data: {
		list: []
	},
	mounted(){
		var vueScope = this;
		axios.get('example1.json')
		.then(function (response) {
			vueScope.list = response.data.sourceControl;
		})
		.catch(function (error) {
			console.log(error);
		});
	}
})

Vue.component('appContainers-tag', {
	props: ['struct'],
	template: '<div class="appContainers">{{ struct }}</div>'
})

var appContainers = new Vue({
	el: '#appContainers-app',
	data: {
		list: []
	},
	mounted(){
		var vueScope = this;
		axios.get('example1.json')
		.then(function (response) {
			vueScope.list = response.data.sourceControl;
		})
		.catch(function (error) {
			console.log(error);
		});
	}
})
