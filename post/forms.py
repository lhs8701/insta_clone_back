from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    photo = forms.ImageField(label='', required=False)  # model에 사진 필드가 이미 있지만, ProcessedImageField는 django 자체 필드가 아니기 때문에 가공 후 전달해야함
    content = forms.CharField(label='', widget=forms.Textarea(attrs={  # 모델에 선언된 content 필드에 조건 추가 (widget) #label은 HTML의 label 태그, widget은 input태그라 생각
        'class': 'post-new-content',
        'rows': 5,
        'cols': 50,
        'placeholder': '140자까지 등록 가능합니다.'
    }))

    class Meta:
        model = Post
        fields = ['photo', 'content']  # 왜 위에 선언해놓고 fields 속성을 정의?

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'comment-form',
        'size':'70px',
        'placeholder':'댓글 달기...',
        'maxlength':'40',
    }))

    class Meta:
        model = Comment
        fields = ['content']