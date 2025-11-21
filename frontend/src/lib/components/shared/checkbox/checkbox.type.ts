import type { HTMLInputAttributes } from "svelte/elements";

export interface CheckBoxProps extends HTMLInputAttributes {
    value?: string;
    label?: string;
    wrapperClass?: string;
}