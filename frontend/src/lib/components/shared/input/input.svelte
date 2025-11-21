<script lang="ts">
    import { Icon } from "svelte-hero-icons";
    import type { InputProps } from "./input.type";

    let { icon, wrapperClass, ...rest }: InputProps = $props();
</script>

<div
    class="flex items-center outline-1 rounded-md py-1 focus-within:outline-primary-color {wrapperClass}"
>
    {#if icon}
        <Icon src={icon} size="24" solid class="ms-3" />
    {/if}
    <input {...rest} class="w-full border-0 outline-0 ring-0 ps-2" />
</div>
