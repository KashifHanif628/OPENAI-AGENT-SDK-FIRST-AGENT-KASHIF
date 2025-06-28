# OPENAI-AGENT-SDK-FIRST-AGENT-KASHIF
This is an OpenAI Agents SDK my First-Agent application. 

# 🔧 OpenAI Agents SDK kya hai?
Ye ek Python tool hai jo aapko "smart AI agents" banane me madad karta hai. Aap soch sakte hain ke ye AI assistants jaise hain jo kaam samajh kar usay khud se solve karte hain — jaise ek chhoti team ho jo Python me kaam kar rahi ho.

# 🧱 Isme kya-kya cheezein hoti hain (Primitive tools)
Agent
Sochiye ek smart banda (AI model) hai, jisko aap instructions dete hain, aur kuch tools use karne dete hain — woh khud se kaam karta hai. Yani teacher ne homework dya or usay kerne k lya as a tool ek book di. 

Handoff
Jab ek agent kisi aur agent se help mangta hai ya kaam delegate karta hai. Jaise ek banda dusre se kehta hai: "ye kaam tum kar lo." ASAN ALFAZ ME AGENT APAS ME KAM BAANT SAKTE HE.

Guardrails
Ye input check karte hain — jaise ke kisi form me galat data ho to turant mana kar diya jaye. Isse agents bekaar input pe kaam nahi karte.


# 🐍 Python ke saath powerful combination
Aap Python ka use karke in agents ko chain kar sakte hain, tools bana sakte hain, aur real-world apps design kar sakte hain — bina zyada complicated cheezein seekhne ke.

# 🔍 Kya extra milta hai SDK me?
Tracing
Aap dekh sakte hain agent ne kya kiya, kaise socha, kis step pe kya decision liya — jaise ek movie ki rewind ho rahi ho debugging ke liye.

Fine-tuning & Evaluation
Aap apne agents ko evaluate kar sakte hain (kaam sahi kar rahe ya nahi), aur zarurat ho to unhe fine-tune bhi kar sakte hain.

# ❓ Agents SDK kyun use karein?
⭐ Simple aur Strong — dono
1- Sikhne me asaan: Sirf kuch basic concepts hain, jyada complexity nahi.
2- Flexible: Shuru se hi kaafi kuch bana sakte hain, aur agar chaahein to kaafi kuch customize bhi kar sakte hain.


# 🧰 Main Features - Aasan Zabaan me
Feature	Matlab
Agent loop	    Agent khud se tool use karta hai, result dekhta hai, agla step decide karta hai — jab tak kaam khatam   
                na ho.
Python-first	Aapko naye frameworks ya syntax nahi seekhne — sab kuch Python me hota hai.
Handoffs	    Agents aapas me kaam baant sakte hain.
Guardrails	    Input check hote hain, galat cheez pe kaam nahi hota.
Function tools	Aap koi bhi Python function ko "tool" bana sakte hain — auto validation ke saath.
Tracing	        Aapka pura agent kaam kaise kar raha hai, wo dekh sakte hain (jaise ek live debug view).

# 💡 Ek chhoti example sochiye:
Aap ek agent banate hain jise bola gaya: “Mujhe ek meeting ka schedule banana hai.”

Agent input check karta hai (Guardrails)

Calendar tool se data nikalta hai (Function tool)

Zarurat ho to kisi dusre agent ko handoff deta hai

Sab kuch trace bhi ho raha hota hai — aap dekh sakte ho ke kya ho raha hai

# INSTALLATIONS.

1- UV (ITS A PACKAGE MANAGER)
uv init first-agent

is se hamare project folder me ek first-agent name ka folder ban jayga vs code me.

2- run this command in the directory folder cmd.

then

pip install openai-agents

or

uv add openai-agents

then go in you vs code main.py file and write code there.

after completed of code please run the below command to sea the agent result.

uv run main.py
