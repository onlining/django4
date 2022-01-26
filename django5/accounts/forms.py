from django import forms
#장고의 forms를 가져옵니다.
from .models import User
#연동시킬 모델인 user모델을 가져옵니다.
from argon2 import PasswordHasher
#비밀번호 암호화에 필요한 클래스를 가져옵니다.

class RegisterForm(forms.ModelForm):
#회원가입 폼 클래스를 생성함과 동시에 forms의 modelform을 상속받습니다.
    user_id =forms.CharField(
        #model로부터 연결시킨 user_id라는 변수명으로 form을 정의합니다. charfield를 이용하였습니다.
        label='아이디',
        #label속성은 django4=1게시글에서 작성한 label 태그의 text에 해당하는 부분입니다
        required=True,
        #required 속성은 필수적으로 입력받아야 하는 필드인지의 여부를 체크합니다. 따라서 true로 설정하면 클라이언트가 데이터를 입력하지 않고 submit할 경우 브라우저
        #화면에 값을 입력하라는 알림창이 뜨게 되는 required

        widget=forms.TextInput(
            attrs={
                'calss': 'user-id',
                'placeholder':'아이디'            }
        
        ),
        error_messages={'required':'아이디를 입력해주세요.'}
        #key에 해당하는 조건이 만족되지 않을 경우 생성할 에러 메시지를 설정하는 부분입니다.
    )
    user_pw=forms.CharField(
        label="비밀번호",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'user-pw',
                'placeholder':'비밀번호'
            }
            ),
            error_messages={'required: 비밀번호를 입력해주세요'}
    )
    user_pw_confirm=forms.CharField(
        label="비밀번호 확인",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'user-pw-confirm',
                'placeholder':'비밀번호 확인'
            }
        ),
        error_messages={'required':'비밀번호가 일치하지 않습니다.'}
    )
    user_name=forms.CharField(
        label="이름",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'user-name',
                'placeholder':'이름'
            }
        ),
        error_messages={'required':'닉네임을 입력해주세요'}
    )
    user_email=forms.EmailField(
        label='이메일',
        required=True,
        
        widget=forms.EmailInput(
            attrs={
                'class':'user-email',
                'placeholder':'이메일'
            }
        ),
        error_messages={'required':'이메일을 입력해주세요'}
    )

    field_order=[
        'user_id',
        'user_pw',
        'user_pw_confirm',
        'user_name',
        'user_email'
    ]
    #추가로 필드 순서를 지정하는 field_order


    class Meta:
        #회원가입폼과 연결시킬 메타데이터들을 입력하는 부분
        model=User
        #유저모델을 연결
        fields=[
            'user_id',
            'user_pw',
            'user_name',
            'user_email'
        ]
        #유저모델중에서 form을 통해 클라이언트로부터 값을 입력받을 필드들만 연결시킵니다.User
    def clean(self):
        cleaned_data=super().clean()
        user_id=cleaned_data.get('user_id','')
        user_pw=cleaned_data.get('user_pw','')
        user_pw_confirm=cleaned_data.get('user_pw_confirm','')
        user_name=cleaned_data.get('user_name','')
        user_email=cleaned_data.get('user_email','')

        if user_pw != user_pw_confirm:
            return self.add_error('user_pw_confirm','비밀번호가 다릅니다')
        elif not(4<=len(user_id)<=16):
            return self.add_error('user_id','아이디는 4~16자로 입력해주세요')
        elif 8> len(user_pw):
            return self.add_error('user_pw','비밀번호는 8자 이상으로 적어주세요')
        else:
            self.user_id=user_id
            self.user_pw=PasswordHasher().hash(user_pw)