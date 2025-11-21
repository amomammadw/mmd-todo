import type { HTMLInputAttributes } from "svelte/elements";
import type { IconSource } from "svelte-hero-icons";

export interface InputProps extends HTMLInputAttributes {
    value?: string;
    icon?: IconSource;
    wrapperClass?: string;
}
