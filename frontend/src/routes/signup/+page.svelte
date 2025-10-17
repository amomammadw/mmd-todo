<script lang="ts">
    import signupimage from "$lib/assets/signup.png"
    import Input from "$lib/components/shared/input/input.svelte";
    import {User, LockClosed, Envelope} from "svelte-hero-icons"
    import Button from "$lib/components/shared/button/button.svelte";
    import Checkbox from "$lib/components/shared/checkbox/checkbox.svelte";
</script>

<div class="rounded-lg flex z-10 h-3/4 w-3/5 min-h-9/12 bg-white">
    <div class="w-full flex items-end justify-start">
        <img src={signupimage} alt="signin" class="h-5/6" />
    </div>
    <div class="w-full flex flex-col px-12 py-12">
        <h1 class="font-bold text-3xl"> Sign Up </h1>
        <Input icon={User} placeholder="Enter First Name" extraclass="mt-6"/>
        <Input icon={User} placeholder="Enter Last Name" extraclass="mt-6"/>
        <Input icon={User} placeholder="Enter Username" extraclass="mt-6"/>
        <Input icon={Envelope} placeholder="Enter Email" extraclass="mt-6"/>
        <Input icon={LockClosed} type="password" placeholder="Enter Password" extraclass="mt-6"/>
        <Input icon={LockClosed} type="password" placeholder="Confirm Password" extraclass="mt-6"/>
        <Checkbox text="I agree to all terms" extraclass="mt-6"/>
        <Button text="Register" extraclass="mt-6"/>
        <div class="flex-auto"></div>
        <span> Already have an account? <a href="/signin" class="text-blue-500">Sign in</a></span>
    </div>
</div>
