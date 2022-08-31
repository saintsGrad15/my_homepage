<template>
	<a class="btn btn-outline-dark"
	   :href="destinationURL"
	   :class="{'tabSelected': _id === tabSelectedId}"
	   :_id=_id>
		<img class="buttonImage" v-if="imageURL !== undefined && imageURL.length > 0" :src="imageURL">
		{{ title }}
	</a>
</template>

<script>
    export default {
        name: "TileButton",

		props: ["title", "imageURL", "destinationURL", "_id", "tabSelectedId"],
    }
</script>

<style scoped>
	a.btn {
		width: 150px;
		height: 150px;

		display: flex;
		flex-direction: column;

		justify-content: space-evenly;
		align-items: center;
	}

	a.btn.tabSelected {
		box-shadow: 0px 0px 5px 3px;
	}

	img.buttonImage {
		max-width: 50px;
		max-height: 50px;
	}
</style>