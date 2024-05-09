from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    admin_group, _ = Group.objects.get_or_create(name='Administradores')
    operario_group, _ = Group.objects.get_or_create(name='Operarios')
    
    # Asignar los permisos para el grupo de Administradores
    permissions = Permission.objects.all()
    admin_group.permissions.set(permissions)
    
    # Asignar permisos de solo lectura al grupo de operarios
    read_permissions = Permission.objects.filter(codename__icontains = 'view')
    operario_group.permissions.set(read_permissions)