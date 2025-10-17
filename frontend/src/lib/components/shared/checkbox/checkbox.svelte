<script lang="ts">
    export let text: string;
    export let extraclass: string = ""
</script>

<div class="flex items-center {extraclass}">
    <input type="checkbox" class="ring-0 outline-0 " />
    <label for="" class="mx-3">{text}</label>
</div>