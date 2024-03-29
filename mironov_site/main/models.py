from django.db import models
from PIL import Image

# Основные парамметры сайта

class SiteSettings(models.Model):
    favicon = models.ImageField(verbose_name="Фавикон сайта")  # Фавикон сайта
    background = models.ImageField(verbose_name="Фон сайта")  # Фон сайта
    contactPhoto = models.ImageField(verbose_name="Фон 'Контакты'")  # Фон страницы Контакты
    name = models.CharField(max_length=50, verbose_name="Имя")  # Имя хозяина сайта
    surname = models.CharField(max_length=50, verbose_name="Фамилия")  # Фамилия хозяина сайта
    photo = models.ImageField(verbose_name="Фото 'О себе'")  # Фото хозяина сайта
    skills = models.TextField(max_length=1000, blank=True, verbose_name="Навыки")  # Навыки и умения
    biography = models.TextField(max_length=1000, blank=True, verbose_name="Биография")  # Биография сайта
    site_quote = models.TextField(max_length=500, blank=True, verbose_name="Цитата")  # Цитата сайта
    owner_site_quote = models.CharField(max_length=50, blank=True, verbose_name="Автор цитаты")  # Автор цитатаы сайта

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Основные параметры'
        verbose_name_plural = 'Основные параметры'


# Образование

class Education(models.Model):
    periodOfStudy = models.TextField(max_length=1000, blank=True, verbose_name="Период обучения")  # Период обучения
    theNameOfTheInstitution = models.TextField(max_length=1000, blank=True,
                                               verbose_name="Название заведения/курсов")  # Название заведения
    receivedSkills = models.TextField(max_length=1000, blank=True,
                                      verbose_name="Полученные умения")  # Полученные умения
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.theNameOfTheInstitution

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


# Значки компаний-партнеров (Сотрудничество)

class Partners(models.Model):
    name = models.TextField(max_length=1000, blank=True, verbose_name="Клиент")  # Имя клиента
    Photos = models.ImageField(blank=True, verbose_name="Лого клиента")  # Лого Клиента
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Сотрудничество'


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название проекта")  # Название проекта
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', blank=True)  # Слаг для отображения

    Preview = models.ImageField(verbose_name="Преью")  # Преью проекта
    Photos1 = models.ImageField(blank=True, verbose_name="Фото 1")  # Фото проекта 1
    Photos2 = models.ImageField(blank=True, verbose_name="Фото 2")  # Фото проекта 2
    Photos3 = models.ImageField(blank=True, verbose_name="Фото 3")  # Фото проекта 3
    Photos4 = models.ImageField(blank=True, verbose_name="Фото 4")  # Фото проекта 4
    Photos5 = models.ImageField(blank=True, verbose_name="Фото 5")  # Фото проекта 5
    Photos6 = models.ImageField(blank=True, verbose_name="Фото 6")  # Фото проекта 6
    Photos7 = models.ImageField(blank=True, verbose_name="Фото 7")  # Фото проекта 7
    Photos8 = models.ImageField(blank=True, verbose_name="Фото 8")  # Фото проекта 8
    Photos9 = models.ImageField(blank=True, verbose_name="Фото 9")  # Фото проекта 9
    Photos10 = models.ImageField(blank=True, verbose_name="Фото 10")  # Фото проекта 10

    linkVK = models.CharField(max_length=50, blank=True, verbose_name="VK")  # Ссылка на ВКонтакте
    linkTwitter = models.CharField(max_length=50, blank=True, verbose_name="Twitter")  # Ссылка на Твиттер
    linkInstagram = models.CharField(max_length=50, blank=True, verbose_name="Instagram")  # Ссылка на Инстаграмм
    linkRarible = models.CharField(max_length=50, blank=True, verbose_name="Rarible")  # Ссылка на Рарибл

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.title
    
    
    
    
    def save(self):
        super().save()
        
        def lowsize(photo):
            img = Image.open(photo)
            if img.height > 1080 or img.width > 1920:
                output_size = (1920, 1080)
                img.thumbnail(output_size)
                img.save(photo)  # , quality=60, optimize=True
        
        img = Image.open(self.Preview.path)
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.Preview.path) 
            
        if self.Photos1.path:
            lowsize(self.Photos1.path) 
        
        if self.Photos2.path:
            lowsize(self.Photos2.path) 
        
        if self.Photos3.path:
            lowsize(self.Photos3.path)    
        
        if self.Photos4.path:
            lowsize(self.Photos4.path) 
        
        if self.Photos5.path:
            lowsize(self.Photos5.path)  
        
        if self.Photos6.path:
            lowsize(self.Photos6.path)    
        
        if self.Photos7.path:
            lowsize(self.Photos7.path)        
        
        if self.Photos8.path:
            lowsize(self.Photos8.path)
        
        if self.Photos9.path:
            lowsize(self.Photos9.path)

        if self.Photos10.path:
            lowsize(self.Photos10.path)
           

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-time_create', 'title']  # Сортировка записей при отображении на сайте



class Creation(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название проекта")  # Название проекта
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', blank=True)  # Слаг для отображения

    Preview = models.ImageField(verbose_name="Преью")  # Преью проекта
    Photos1 = models.ImageField(blank=True, verbose_name="Фото 1")  # Фото проекта 1
    Photos2 = models.ImageField(blank=True, verbose_name="Фото 2")  # Фото проекта 2
    Photos3 = models.ImageField(blank=True, verbose_name="Фото 3")  # Фото проекта 3
    Photos4 = models.ImageField(blank=True, verbose_name="Фото 4")  # Фото проекта 4
    Photos5 = models.ImageField(blank=True, verbose_name="Фото 5")  # Фото проекта 5
    Photos6 = models.ImageField(blank=True, verbose_name="Фото 6")  # Фото проекта 6
    Photos7 = models.ImageField(blank=True, verbose_name="Фото 7")  # Фото проекта 7
    Photos8 = models.ImageField(blank=True, verbose_name="Фото 8")  # Фото проекта 8
    Photos9 = models.ImageField(blank=True, verbose_name="Фото 9")  # Фото проекта 9
    Photos10 = models.ImageField(blank=True, verbose_name="Фото 10")  # Фото проекта 10

    linkVK = models.CharField(max_length=50, blank=True, verbose_name="VK")  # Ссылка на ВКонтакте
    linkTwitter = models.CharField(max_length=50, blank=True, verbose_name="Twitter")  # Ссылка на Твиттер
    linkInstagram = models.CharField(max_length=50, blank=True, verbose_name="Instagram")  # Ссылка на Инстаграмм
    linkRarible = models.CharField(max_length=50, blank=True, verbose_name="Rarible")  # Ссылка на Рарибл

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.title


    def save(self):
        super().save()
        
        def lowsize(photo):
            img = Image.open(photo)
            if img.height > 1080 or img.width > 1920:
                output_size = (1920, 1080)
                img.thumbnail(output_size)
                img.save(photo)  # , quality=60, optimize=True
        
        img = Image.open(self.Preview.path)
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.Preview.path) 
            
        # if self.Photos1.path:
        #     lowsize(self.Photos1.path) 
        
        # if self.Photos2.path:
        #     lowsize(self.Photos2.path) 
        
        # if self.Photos3.path:
        #     lowsize(self.Photos3.path)    
        
        # if self.Photos4.path:
        #     lowsize(self.Photos4.path) 
        
        # if self.Photos5.path:
        #     lowsize(self.Photos5.path)  
        
        # if self.Photos6.path:
        #     lowsize(self.Photos6.path)    
        
        # if self.Photos7.path:
        #     lowsize(self.Photos7.path)        
        
        # if self.Photos8.path:
        #     lowsize(self.Photos8.path)
        
        # if self.Photos9.path:
        #     lowsize(self.Photos9.path)

        # if self.Photos10.path:
        #     lowsize(self.Photos10.path)

    class Meta:
        verbose_name = 'Креативный проект'
        verbose_name_plural = 'Креативные проекты'
        ordering = ['-time_create', 'title']  # Сортировка записей при отображении на сайте

