<script lang="ts">
    import signinimage from "$lib/assets/signin.png"
    import Input from "$lib/components/shared/input/input.svelte";
    import {User, LockClosed} from "svelte-hero-icons"
    import Button from "$lib/components/shared/button/button.svelte";
    import Checkbox from "$lib/components/shared/checkbox/checkbox.svelte";
</script>

<div class="rounded-lg flex z-10 h-3/4 w-3/5 min-h-9/12 bg-white">
    <div class="w-full flex flex-col px-12 py-24">
        <h1 class="font-bold text-3xl"> Sign In </h1>
        <Input icon={User} placeholder="Enter Username" extraclass="mt-6"/>
        <Input icon={LockClosed} type="password" placeholder="Enter Password" extraclass="mt-6"/>
        <Checkbox text="Remember Me" extraclass="mt-6"/>
        <Button text="Login" extraclass="mt-6"/>
        <div class="flex-auto"></div>
        <span> Don't have an account? <a href="/signup" class="text-blue-500">Create One</a></span>
    </div>
    <div class="w-full flex items-end justify-end">
        <img src={signinimage} alt="signin" class="h-5/6" />
    </div>
</div>
