<script lang="ts">
    import AuthLayout from '$lib/components/layout/auth/auth.svelte';
	
	let { children } = $props();
</script>

<AuthLayout>
	{@render children?.()}
</AuthLayout>
