<script lang="ts">
    import type {CheckBoxProps} from "./checkbox.type"

    let { label, wrapperClass, ...rest }: CheckBoxProps = $props();
</script>

<div class="flex items-center {wrapperClass}">
    <input {...rest} type="checkbox" class="ring-0 outline-0 " />
    <label for="" class="mx-3">{label}</label>
</div>