<script lang="ts">
    import { Icon, type IconSource } from "svelte-hero-icons";
    export let icon: IconSource | null = null;
    export let type: "password" | "text" = "text"
    export let placeholder: string = ""
    export let extraclass: string = ""
</script>

<div class="flex items-center outline-1 rounded-md py-1 focus-within:outline-primary-color {extraclass}">
    {#if icon}
        <Icon src={icon} size="24" solid class="ms-3"/>
    {/if}
    <input {type} class="w-full border-0 outline-0 ring-0 ps-2" {placeholder}/>
</div>


