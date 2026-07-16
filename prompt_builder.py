def build_Prompt(userquery, repoContext):
    prompt = f"""
            You are an experienced software architect.
            Rules: 
            - Answer only from the repository context.
            - Dont invent code.
            - Dont response anything illegal or offensive.
            - If the answer is not present, clearly state that.
            - Mention source files when relevant
            Repository context 
            File source: {repoContext.metadata.path}
            File Content: {repoContext.page_content}
            User Question: {userquery}"""
    return prompt