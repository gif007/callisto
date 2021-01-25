

def get_mech_by_user(MobileSuit, User, request):

    return MobileSuit.objects.filter(
        controller=User.objects.filter(
        username=request.user.get_username()
        ).get()
        ).get()