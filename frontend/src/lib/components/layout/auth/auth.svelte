<script lang="ts">
	import signupbg from '$lib/assets/signup-bg.png';

</script>

<div class="bg-primary-color h-full w-full flex items-center justify-center">
    <slot />
    <!-- TODO: use div and set background property -->
    <img src={signupbg} alt="signin pages background" class="fixed left-0 top-0"/>
</div>