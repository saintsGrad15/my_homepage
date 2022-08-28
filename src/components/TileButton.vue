<template>
	<a :href="destinationURL">
		<button class="tileBtn btn btn-outline-dark">
			<img class="buttonImage" v-if="imageURL !== undefined && imageURL.length > 0" :src="imageURL">
			{{ title }}
		</button>
	</a>
</template>

<script>
    export default {
        name: "TileButton",

		props: ["title", "imageURL", "destinationURL"]
    }
</script>

<style scoped>
	button.tileBtn
	{
		width: 150px;
		height: 150px;

		display: flex;
		flex-direction: column;

		justify-content: space-evenly;
		align-items: center;
	}

	img.buttonImage
	{
		max-width: 50px;
		max-height: 50px;
	}
</style>