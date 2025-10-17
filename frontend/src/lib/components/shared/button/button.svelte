<script lang="ts">
    export let text: string;
    export let extraclass: string = ""
</script>

<span>
    <button class="bg-primary-color my-2 py-3 px-4 rounded-md hover:opacity-90 {extraclass}">{text}</button>
</span>