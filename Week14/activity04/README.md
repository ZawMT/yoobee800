## Week 14 - Activity 4:  Application of Decorator in your MSE800.2 project (group activity)
Refine and extend your ongoing MSE800.2 project by incorporating the use of Python decorators. Ensure that you clearly demonstrate how decorators are applied within your implementation and provide a concise explanation of their purpose and impact in the context of your project. Share the result as maximum two page short report and add the report into your GitHub and share the link here.

### Usage in the assessment project
Python's built-in decorator, @classmethod, is used as follows:
`class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username
        token["email"] = user.email

        return token`

The class TokenObtainPairSerializer (JTW framework) already has a function called get_token, but that function doesn't include some info (here, username and email) in the return information. So the function is modified for that part - to include those info in the return - using help of decorator.