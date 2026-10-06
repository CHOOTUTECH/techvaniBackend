from django.core.management.base import BaseCommand
from blog.models import Category, Author, Tag, Article, StaticPage, Comment

class Command(BaseCommand):
    help = 'Seeds all 17 initial Hindi tech articles, categories, authors, and pages into database'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("TechVani डेटाबेस सीडिंग प्रारंभ हो रही है..."))

        # 1. Categories
        categories_data = [
            {'name': 'मुख्य पृष्ठ', 'slug': 'home', 'description': 'टेकवाणी के सभी ताज़ा लेख और ट्रेंडिंग टेक विश्लेषण', 'icon': 'home'},
            {'name': 'प्रोग्रामिंग', 'slug': 'programming', 'description': 'पायथन, जावास्क्रिप्ट, वेब डेवलपमेंट और सॉफ्टवेयर इंजीनियरिंग गाइड', 'icon': 'terminal', 'meta_title': 'प्रोग्रामिंग ट्यूटोरियल – पायथन, जावास्क्रिप्ट और वेब डेवलपमेंट', 'meta_description': 'सरल हिंदी में प्रोग्रामिंग सीखें। शुरुआती से लेकर एडवांस लेवल तक की संपूर्ण गाइड।'},
            {'name': 'कीबोर्ड शॉर्टकट्स', 'slug': 'keyboard-shortcuts', 'description': 'विंडोज, मैक, एक्सेल, वीएस कोड और ब्राउज़र के उत्पादक शॉर्टकट्स', 'icon': 'keyboard', 'meta_title': 'कंप्यूटर कीबोर्ड शॉर्टकट्स – विंडोज, मैक, एक्सेल व ब्राउज़र', 'meta_description': 'उत्पादकता 2x बढ़ाने वाले शीर्ष कीबोर्ड शॉर्टकट्स हिंदी में।'},
            {'name': 'कंप्यूटर ट्रिक्स', 'slug': 'computer-tricks', 'description': 'छिपे हुए सिस्टम टूल्स, विंडोज रन कमांड्स और स्पीड ऑप्टिमाइजेशन टिप्स', 'icon': 'laptop_windows', 'meta_title': 'कंप्यूटर ट्रिक्स और सीक्रेट्स – पीसी को सुपरफास्ट बनाएं', 'meta_description': 'विंडोज रन कमांड्स, सिस्टम टूल्स और कैश क्लीनअप के आसान तरीके।'},
            {'name': 'गैजेट्स', 'slug': 'gadgets', 'description': 'लैपटॉप, मॉनिटर्स, मैकेनिकल कीबोर्ड्स और स्मार्ट एक्सेसरीज की निष्पक्ष समीक्षा', 'icon': 'devices', 'meta_title': 'गैजेट्स और हार्डवेयर समीक्षाएं – निष्पक्ष बेंचमार्क व रेटिंग्स', 'meta_description': 'कोडिंग लैपटॉप्स, अल्ट्रावाइड मॉनिटर्स और मैकेनिकल कीबोर्ड्स की गहन समीक्षा।'},
            {'name': 'सॉफ्टवेयर', 'slug': 'software', 'description': 'डेस्कटॉप सॉफ्टवेयर, यूटिलिटीज, उत्पादकता ऐप्स और ओएस टूल्स', 'icon': 'apps', 'meta_title': 'सॉफ्टवेयर और यूटिलिटीज – विंडोज और मैक के बेहतरीन टूल्स', 'meta_description': 'दैनिक कार्य और कोडिंग के लिए आवश्यक सॉफ्टवेयर गाइड।'},
            {'name': 'टेक गाइड', 'slug': 'tech-guides', 'description': 'चरण-दर-चरण तकनीकी ट्यूटोरियल और समस्या निवारण गाइड्स', 'icon': 'menu_book', 'meta_title': 'टेक गाइड्स – आसान हिंदी तकनीकी ट्यूटोरियल्स', 'meta_description': 'स्टेप-बाय-स्टेप टेक गाइड्स और व्यावहारिक समाधान।'},
        ]
        cat_map = {}
        for c in categories_data:
            cat, _ = Category.objects.get_or_create(slug=c['slug'], defaults=c)
            cat_map[c['slug']] = cat

        # 2. Authors
        authors_data = [
            {'name': 'राहुल शर्मा', 'role': 'सीनियर टेक एडिटर & सिस्टम्स आर्किटेक्ट', 'avatar': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDRqWTnK78J57cA3pwd5P5LdLh8F9h4rmJvHKVLcd74gYLfIwO19L_GFdjQzG_CA4RhcXrex_xwxWVvanO9E_vgOJDO35mRbtADBom8MMtNCtF32plRqivyAoBrQSHRNfWounA1j6UdCqNOVGePsQnGc7hOMkOdLEsb37n6WE3cchoml3sIO0T96lBICb9iTVkpNTx7Ky1k_zmCPPcx1lSMiGyTRtXnglEJNMLoV_cKw-QXuTqJ9YSU', 'bio': '10+ वर्षों का सिस्टम एडमिनिस्ट्रेशन और विंडोज/लिनक्स आर्किटेक्चर का अनुभव। टेकवाणी के प्रधान संपादक।', 'twitter': '@rahul_techvani', 'articles_count': 142},
            {'name': 'अमन वर्मा', 'role': 'हार्डवेयर और गैजेट स्पेशलिस्ट', 'avatar': 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=200&q=80', 'bio': 'गेमिंग रिग्स, कस्टम मैकेनिकल कीबोर्ड्स और वर्कस्टेशन बेंचमार्क्स के विशेषज्ञ।', 'twitter': '@aman_gadgets', 'articles_count': 88},
            {'name': 'प्रिया देसाई', 'role': 'फ्रंटएंड डेवलपर & डिस्प्ले एनालिस्ट', 'avatar': 'https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=200&q=80', 'bio': 'React, Next.js और अल्ट्रावाइड डिस्प्ले वर्कफ्लो पर तकनीकी गाइड लिखती हैं।', 'twitter': '@priya_codes', 'articles_count': 65},
            {'name': 'विक्रम राठौर', 'role': 'AI & पायथन इंजीनियर', 'avatar': 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?auto=format&fit=crop&w=200&q=80', 'bio': 'पायथन, मशीन लर्निंग और ओपन-सोर्स डेवलपमेंट के शौकीन।', 'twitter': '@vikram_py', 'articles_count': 94},
        ]
        auth_map = {}
        for a in authors_data:
            auth, _ = Author.objects.get_or_create(name=a['name'], defaults=a)
            auth_map[a['name']] = auth

        # 3. Tags
        tags_list = ['Python', 'JavaScript', 'Windows11', 'ExcelTricks', 'MacBookM3', 'VSCode', 'AIटूल्स', 'CyberSecurity', 'React19', 'GitHub', 'Linux']
        tag_map = {}
        for t in tags_list:
            tag_obj, _ = Tag.objects.get_or_create(name=t, defaults={'slug': t.lower()})
            tag_map[t] = tag_obj

        # 4. All 17 Articles Data
        articles_data = [
            # Main Hero
            {
                'title': 'विंडोज 11 के 25 सबसे उपयोगी कीबोर्ड शॉर्टकट्स जो आपका समय 2x बचाएंगे',
                'slug': 'windows-11-25-useful-keyboard-shortcuts',
                'excerpt': 'डेस्कटॉप स्विचिंग, वर्चुअल वर्कस्पेस, क्लिपबोर्ड हिस्ट्री और टर्मिनल एक्सेस को सहज बनाकर अपने दैनिक कंप्यूटर कार्य को सुपरचार्ज करें।',
                'content': 'विंडोज 11 में यदि आप केवल माउस पर निर्भर रहते हैं तो समय बर्बाद होता है। Win + V से क्लिपबोर्ड हिस्ट्री खोलें। Win + Shift + S से स्निपिंग टूल चलाएं। Win + Ctrl + D से नया वर्चुअल डेस्कटॉप बनाएं।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuD1ME4gn0MqYe9-DVvwUTtan8Il5QbOWj1hGOwNQepSzUG3U7bZKPaPCHuHhXnyRW5yj85zdo5sGjijw6URRPOZAyJ3Dk-MVNSsDg7xluRng9UzrBB-qSiyzl0seSH1jg0CIy4fRF2BltHo3_3ySoTccGc4P42gZdisKtjd8P1W5DymOzZMMRpFP0ohbnG2BY9WtZljmvmUZI7OY_ELHE6JEUpuQBbWq7VuWmt7CVOHkJNfOyeyN--S',
                'category': cat_map['keyboard-shortcuts'],
                'author': auth_map['राहुल शर्मा'],
                'meta_title': 'विंडोज 11 के 25 कीबोर्ड शॉर्टकट्स (2025) – टेकवाणी गाइड',
                'meta_description': 'डेस्कटॉप स्विचिंग, वर्चुअल वर्कस्पेस, क्लिपबोर्ड हिस्ट्री और टर्मिनल एक्सेस को सहज बनाकर अपने दैनिक कंप्यूटर कार्य को सुपरचार्ज करें।',
                'keywords': 'विंडोज 11, कीबोर्ड शॉर्टकट्स, कंप्यूटर ट्रिक्स',
                'schema_type': 'HowTo',
                'featured_order': 1,
                'is_featured': True,
                'is_editorial_choice': True,
                'is_trending': True,
                'reading_time_minutes': 5,
                'views_count': 38420,
                'tags': ['Windows11', 'ExcelTricks'],
            },
            # Sub Hero 1
            {
                'title': 'पायथन (Python) 2025 में स्क्रैच से कैसे सीखें: संपूर्ण शुरुआती गाइड',
                'slug': 'python-learn-from-scratch-2025-guide',
                'excerpt': 'वेरिएबल्स, लूप्स, फंक्शन्स और डेटा स्ट्रक्चर्स से शुरुआत करके AI और वेब डेवलपमेंट तक का सटीक रोडमैप।',
                'content': 'पायथन 2025 की नंबर-1 प्रोग्रामिंग भाषा है। इसका सरल सिंटैक्स और शक्तिशाली लाइब्रेरीज़ इसे शुरुआती छात्रों के लिए सर्वश्रेष्ठ बनाती हैं।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCkCaZ_3J6M89Us5yc3DBSxygCptlkOakb-IcII__ChqgFEcvyQ0YO7nwYz0TcrDgaPy2AG2Xrim1fucr0mq6qmZWnlzxVNNXkMmvNTY7Rave_ZoQZbkRzniPFyOZAi17T0QCkAm0W8vZUzi7bN-eygrAkW6nVeRu6mrRqZDtEYQwp9TScNVfN26fmz65nw2z4DKzRfe3ghLFtPbM6kx_S8mARwfCU2UCkgsTRMjzioXaEhDbnzgn89',
                'category': cat_map['programming'],
                'author': auth_map['विक्रम राठौर'],
                'meta_title': 'पायथन स्क्रैच से सीखें (2025) – संपूर्ण हिंदी गाइड',
                'meta_description': 'पायथन प्रोग्रामिंग का 4-चरणीय रोडमैप। वेरिएबल्स से लेकर Django और AI तक।',
                'keywords': 'पायथन, प्रोग्रामिंग, AIटूल्स, कोडिंग',
                'schema_type': 'TechArticle',
                'featured_order': 2,
                'is_featured': True,
                'is_trending': True,
                'reading_time_minutes': 8,
                'views_count': 29140,
                'tags': ['Python', 'AIटूल्स'],
            },
            # Sub Hero 2
            {
                'title': 'M3 चिपसेट वाले नए लैपटॉप्स: क्या यह भारी कोडिंग और AI मॉडल्स के लिए बेस्ट हैं?',
                'slug': 'm3-chipset-laptops-coding-ai-benchmark-review',
                'excerpt': '3nm आर्किटेक्चर, यूनिफाइड मेमोरी परफॉर्मेंस और लोकल LLMs रन करने की क्षमता का गहन तकनीकी विश्लेषण।',
                'content': 'एप्पल के 3nm वाले M3 Pro और Max चिपसेट ने लैपटॉप कंप्यूटिंग को बदल दिया है। Docker बिल्ड टाइम 45% तेज और 20+ घंटे की बैटरी लाइफ मिलती है।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCkNv6p6Xei4LBadkqfpDfN0dNFXSBprj5J8ykMoR6EUtozxN7a5x4btY4X_77CmYxUneuk9mSaL03p3FtG4mGcZvr94p1OzFIsAq2nlekCvGPvmZIz771nDaEhSKeMR_OORJTBpo_ulnulMq0mWtMr5o8FOIcf00Zy1TPbFPka9UjTtLzxt6nnB7R720k96O9ppDzOPz7Zj-CVlDuL4D5s1MTQ6AxQUDjkUzUbCBdquJZKm9BZpLZX',
                'category': cat_map['gadgets'],
                'author': auth_map['अमन वर्मा'],
                'meta_title': 'MacBook Pro M3 चिपसेट समीक्षा (2025) – रेटिंग 9.2/10',
                'meta_description': 'क्या नया M3 मैकबुक कोडिंग और AI के लिए बेस्ट है? जानिए बेंचमार्क्स और बैटरी टेस्ट।',
                'keywords': 'MacBookM3, गैजेट्स, हार्डवेयर',
                'schema_type': 'Product',
                'rating': 9.2,
                'product_price': '₹1,69,900',
                'featured_order': 3,
                'is_featured': True,
                'is_trending': True,
                'reading_time_minutes': 6,
                'views_count': 18560,
                'tags': ['MacBookM3', 'AIटूल्स'],
            },
            # Programming Corner 1
            {
                'title': 'VS Code के 10 सुपर एक्सटेंशन्स जो हर सॉफ्टवेयर डेवलपर को चाहिए',
                'slug': 'top-10-vs-code-extensions-developers-2025',
                'excerpt': 'कोड ऑटोकम्प्लीशन से लेकर लाइव डीबगिंग तक, ये 10 एक्सटेंशन आपके प्रोजेक्ट को तीव्र गति देंगे।',
                'content': '1. Prettier - कोड फॉर्मेटिंग\n2. GitLens - गिट इतिहास\n3. Error Lens - इनलाइन एरर डिटेक्शन\n4. Auto Rename Tag - HTML टैग्स',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDZTkNs7ourFJgwCfsUD7p6mr0GI2zBNR7s71JP0bJXIf9uGwFzJDLGYMolNG6-rUmhKh8fz_RxaskwRcqMl8TNAWa6Ub9yJ6NPYXYF0KzRPT1PH_45hrJqtCDb17nBOi-ezRmgwRSd-MNYGnJnrHS7QhgG2v26uYVf5gyhsTTzgDzfp8K9FtlSoIb6WtA_URdAJoT2SfPMC7_nNdX-TFzoFJvhqRfz90mFp8W4DDArBvcu5uX5n70t',
                'category': cat_map['programming'],
                'sub_category': 'टूलकिट',
                'author': auth_map['राहुल शर्मा'],
                'meta_title': 'VS Code के 10 बेस्ट एक्सटेंशन्स (2025) – डेवलपर टूलकिट',
                'meta_description': 'कोड ऑटोकम्प्लीशन से लाइव डीबगिंग तक 10 एक्सटेंशन।',
                'schema_type': 'TechArticle',
                'reading_time_minutes': 4,
                'views_count': 22400,
                'tags': ['VSCode', 'JavaScript'],
            },
            # Programming Corner 2
            {
                'title': 'Git और GitHub कैसे काम करते हैं: शुरुआती डेवलपर्स के लिए स्टेप-बाय-स्टेप गाइड',
                'slug': 'git-and-github-explained-beginners-guide',
                'excerpt': 'ब्रांचिंग, मर्जींग और पुल रिक्वेस्ट के बुनियादी कॉन्सेप्ट्स को सरल व्यावहारिक उदाहरणों से समझें।',
                'content': 'Git एक डिस्ट्रिब्यूटेड वर्जन कंट्रोल सिस्टम है। git init, git add, git commit और git push का आसान हिंदी ट्यूटोरियल।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAE9LWqJ6fzuEMyKkTcpnVEj0R8I5NjubrMBTNAFvEFYbcvx4_UmXh88ny3Uknvputruk6VCngGBhQgFS1v8YHGRhI5nvIjj-0rNjy9tbbImJA5biLpeVZbqgnGD6_qiLCsDSF3O4MrNMetJ2HK0UAGIJUxZsDBhbzV-RV7oXy4nqmDTqo2QyJ_Uc3VVey5MKSaFNKR0ILV_d-SRJsA-k-VXO0PK7ARFAi0wl2b3pmLxsQI8snG54YC',
                'category': cat_map['programming'],
                'sub_category': 'Web Dev',
                'author': auth_map['राहुल शर्मा'],
                'meta_title': 'Git और GitHub शुरुआती गाइड हिंदी में',
                'meta_description': 'ब्रांचिंग, मर्जींग और पुल रिक्वेस्ट स्टेप-बाय-स्टेप सीखें।',
                'schema_type': 'TechArticle',
                'reading_time_minutes': 5,
                'views_count': 19800,
                'tags': ['GitHub', 'Linux'],
            },
            # Programming Corner 3
            {
                'title': 'React 19 के नए फीचर्स: सर्वर एक्शन्स और नए कंपाइलर के साथ बड़ा बदलाव',
                'slug': 'react-19-new-features-server-actions-compiler',
                'excerpt': 'मेमोराइजेशन की झंझट खत्म! जानें कैसे React Compiler आपके कोड को अपने आप ऑप्टिमाइज़ करता है।',
                'content': 'React 19 में React Compiler आ गया है जो useMemo और useCallback को ऑटोमैटिक बना देता है। Server Actions से फॉर्म सीधे हैंडल होते हैं।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAjeD3u9DIwCZq6n2YeNMcxN-OkRCRIOHhXusL8kuaSxb41lTuSnfOMyQcTMWUuqRoCyQbCC3VemaP-TrtveJ93ETgZi9K6my8OEa8_BzR3oUfWn7zm0uKcoLC8zAT2cOEpydxqUR-pAiWvxx_gqwrairSVaFkPDxlJLodqhFMgBXj3PmvZgyqSE_EXXQ2tEWHpRawirWNsjoHqSF9QUavDnjKTkmv2pQN43keIq5ANZn03cpISbsBO',
                'category': cat_map['programming'],
                'sub_category': 'JavaScript',
                'author': auth_map['प्रिया देसाई'],
                'meta_title': 'React 19 के नए फीचर्स – कंपाइलर और सर्वर एक्शन्स',
                'meta_description': 'React 19 के सभी मुख्य बदलावों का हिंदी विश्लेषण।',
                'schema_type': 'TechArticle',
                'reading_time_minutes': 5,
                'views_count': 16750,
                'tags': ['React19', 'JavaScript'],
            },
            # Shortcut 1
            {
                'title': 'MS Excel के जादुई शॉर्टकट्स: घंटों का भारी डेटा केवल कुछ मिनटों में सॉर्ट करें',
                'slug': 'ms-excel-magical-shortcuts-productivity',
                'excerpt': 'फ्लैश फिल (Ctrl + E), ऑटो-सम और पिवट टेबल जनरेटर जैसे 12 पावर शॉर्टकट्स जो हर ऑफिस प्रोफेशनल के पास होने चाहिए।',
                'content': 'Ctrl + Shift + L से फिल्टर लगाएं। Alt + = से ऑटो सम करें। Ctrl + E से फ्लैश फिल चलाएं।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCTTsEPtbEZgr-6iHKZRpAxLm2BE5TGBOPGIRdzwrHUF-jtzOSGMHgPNzcRbNiJCi8zRmbkerhNw3mPClAdZm3OYxx1c1eeRCOjbE5gximG6-AuyN3KrEvOeLFdOzWEut2lBblaARaqitunDwd4Xru7QrlzGc4sKhjFjxvFn3qybtEfFC8Gqmksx_uhhmxuL7UrdSBIV8WS5lobQiyDJdJm7JodtbaZ1C8V52hEiUXWGeuAsvAgpyBc',
                'category': cat_map['keyboard-shortcuts'],
                'author': auth_map['राहुल शर्मा'],
                'meta_title': 'MS Excel 12 पावर शॉर्टकट्स – डेटा सॉर्टिंग ट्रिक्स',
                'meta_description': 'घंटों का एक्सेल डेटा मिनटों में सॉर्ट करें इन शॉर्टकट्स से।',
                'schema_type': 'HowTo',
                'reading_time_minutes': 3,
                'views_count': 31200,
                'tags': ['ExcelTricks'],
            },
            # Shortcut 2
            {
                'title': 'विंडोज में छिपे 7 सीक्रेट रन (Run) कमांड्स जो आपके कंप्यूटर को तुरंत तेज़ कर देंगे',
                'slug': '7-secret-windows-run-commands-speed-up-pc',
                'excerpt': 'बिना किसी थर्ड-पार्टी सॉफ्टवेयर के जंक कैश फाइल्स साफ करें, रिसोर्स मॉनिटर खोलें और नेटवर्क रीसेट करें।',
                'content': 'Win + R दबाकर %temp% साफ करें। cleanmgr से डिस्क क्लीनअप करें। resmon से मेमोरी जांचें।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDd9R5JW3QL7MJ9iQkd20nG1avMegiWhNHBBOHLrLiSMT8CSnIjnsADEp1nrCwYSQRMbmrls1MnqD9l1nndMyj-Hcvq3b-Z_VodVr8j8zN4n1CXorO-Go63zBrVvZ5pGIHBzlC4s_xbrVevmSF6Dv9U3dLDtkh6CdVPsePNgv2b3lwrn6hmPR_e-pBte0dvejbmD5g1zkbceljdHl6nva6_kwQcpsyQyALbOG9byI1TDnM5b8puBod3',
                'category': cat_map['computer-tricks'],
                'author': auth_map['राहुल शर्मा'],
                'meta_title': '7 सीक्रेट विंडोज Run कमांड्स – कंप्यूटर तुरंत तेज करें',
                'meta_description': 'बिना किसी एंटीवायरस के पीसी की सफाई और स्पीड बूस्ट।',
                'schema_type': 'HowTo',
                'reading_time_minutes': 4,
                'views_count': 27400,
                'tags': ['Windows11'],
            },
            # Shortcut 3
            {
                'title': 'गूगल क्रोम के 8 टैब मैनेजमेंट शॉर्टकट्स: 50+ खुले टैब्स को बिना हैंग किए संभालें',
                'slug': 'google-chrome-8-tab-management-shortcuts',
                'excerpt': 'गलती से बंद हुआ टैब तुरंत दोबारा खोलें (Ctrl + Shift + T) और विभिन्न प्रोजेक्ट्स के लिए टैब ग्रुप्स को पिन करना सीखें।',
                'content': 'Ctrl + Shift + T अंतिम टैब री-ओपन करता है। Ctrl + Tab अगले टैब पर जाता है। Ctrl + W वर्तमान टैब बंद करता है।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAc_P7_qLYGvQJdorhV0Z_eHBmFEAVXicXyIXKLgVch1-dLp2WmHLSqt8Jv5y9S0wNOo4q_tv8yv9L8m8L0Wp3Wd6MFRQUkSL_xG7rwFyjqSfPrn0DRUzpw11x-OHcDhmgy4OesjW6S8QBFKdUIVhvozTOAKnWLhDe8LOfdWF8uVg7SLve2LaMEF6-XNNcnWWfwWelA7nxfj9nrMURcM_xP_3_ZXRHE1j7B_7GC5cmMAPCTA7zHaY1a',
                'category': cat_map['keyboard-shortcuts'],
                'author': auth_map['प्रिया देसाई'],
                'meta_title': 'Google Chrome 8 टैब मैनेजमेंट शॉर्टकट्स',
                'meta_description': '50+ टैब्स को बिना हैंग किए क्रोम ब्राउज़र में प्रबंधित करें।',
                'schema_type': 'HowTo',
                'reading_time_minutes': 3,
                'views_count': 24100,
                'tags': ['JavaScript'],
            },
            # Video Tutorial
            {
                'title': 'पायथन क्रैश कोर्स 2025: सिर्फ 1 घंटे में पूरे बेसिक्स समझें',
                'slug': 'python-crash-course-2025-1-hour-complete-basics',
                'excerpt': 'वेरिएबल्स, लूप्स, फंक्शन्स और ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग को आसान हिंदी में व्यावहारिक उदाहरणों के साथ लाइव कोड करके समझें।',
                'content': '58 मिनट का संपूर्ण पायथन ट्यूटोरियल। वेरिएबल्स, कंडीशनल्स, लूप्स और मिनी प्रोजेक्ट्स शामिल हैं।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAmPzrlAUiG9ZVqrh8oGAOW6-woIw2-JfVQ-vKXrCPVZldMLc3aT5hc6AzZYeJauiyFT4ko0xlYNUS4gHxThphgKygR-pIH7831qQsre1GU_ekXSm54K_UwUK3-uUrBu5YKEJkB2bIVdYguSJkYyBwifrqHJm1tEg0Oen8TwWWddXqByrYy-_8p2QSQXCB8XA0QX0K_OX0hkHddY9UWjRgQl600p2TsR_1rjm-WE6nKr7J_wXI96wZe',
                'category': cat_map['programming'],
                'author': auth_map['विक्रम राठौर'],
                'meta_title': 'पायथन क्रैश कोर्स 2025 (1 घंटा) – हिंदी वीडियो ट्यूटोरियल',
                'meta_description': 'पायथन बेसिक्स 1 घंटे में लाइव कोड उदाहरणों के साथ सीखें।',
                'video_duration': '58 मिनट',
                'schema_type': 'TechArticle',
                'reading_time_minutes': 58,
                'views_count': 45200,
                'tags': ['Python', 'AIटूल्स'],
            },
            # Hardware Review 1
            {
                'title': 'मैकेनिकल कीबोर्ड vs मेम्ब्रेन: कोडिंग और टाइपिंग स्पीड के लिए कौन सा बेहतर है?',
                'slug': 'mechanical-keyboard-vs-membrane-coding-speed-review',
                'excerpt': 'ब्राउन, रेड और ब्लू स्विच के अंतर, टाइपिंग ध्वनि और लंबे समय तक कोडिंग करते समय हाथों की थकान पर विस्तृत विश्लेषण।',
                'content': 'मैकेनिकल कीबोर्ड टाइपिंग स्पीड 15-20% बढ़ाता है और हाथों की थकान कम करता है। ब्राउन स्विच कोडिंग के लिए सबसे शांत और टैक्टाइल हैं।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuADzMSTV3RuRgJEd55sHvpwH_AlcCyATK3-ZtfMvWo0KLEd0ScjCT5RuZvthCpNd4Gr1wH6INzPc88N-iG7ZtjmBId-f6pUT-K11EV6R1_9izUqtPmrXOi74tBnetDmjKYCh_eL3zfii4RYQ7eGqdUrB596MU6ZMGX04WN1QKBMhXE4sW5sZTM8XWqICH_1xvozS--luGc_iwv954Ho3ZlN9ESZf2jS32zRmzHkamXerb2UJ0R17Sc6',
                'category': cat_map['gadgets'],
                'author': auth_map['अमन वर्मा'],
                'meta_title': 'मैकेनिकल vs मेम्ब्रेन कीबोर्ड – कोडिंग स्पीड रिव्यू (9.4/10)',
                'meta_description': 'स्विच प्रकार, टाइपिंग सटीकता और लॉन्ग-टर्म कम्फर्ट विश्लेषण।',
                'schema_type': 'Product',
                'rating': 9.4,
                'product_price': '₹3,499 - ₹12,999',
                'reading_time_minutes': 6,
                'views_count': 34100,
                'tags': ['VSCode'],
            },
            # Hardware Review 2
            {
                'title': '34-इंच अल्ट्रावाइड कोडिंग मॉनिटर्स: क्या दोहरे मॉनिटर्स से बेहतर है एक सिंगल कर्व्ड स्क्रीन?',
                'slug': '34-inch-ultrawide-monitor-vs-dual-screens-coding-review',
                'excerpt': 'मल्टीटास्किंग, रंग सटीकता, IPS पैनल रिफ्रेश रेट्स और वर्कस्टेशन केबल्स की सफाई के मामले में गहन समीक्षा।',
                'content': '34-इंच अल्ट्रावाइड मॉनिटर बीच के बेज़ल को खत्म करता है और एक ही टाइप-सी केबल से डिस्प्ले और चार्जिंग दोनों संभालता है।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuA-ttrNIe8miVSpxKn7RBtBdoXEyzueuWV8JtraIyBrB2R_6DukwpLM-RpTKmeG6FPg13e1_bW1Y53qhRSvj-BD1In9U_UCLgTgwLABPdaGqUG5msmGJE-fz6GrAf-baDcPAqj9wUeGrRs9qKMQOfUQyTmGAC46fw6GKD1DAE7vtl3E28vXxan6pbO09SoSPn8EuOGFoSLh5QgdCZ5caVIv8b2306NRnaeZa1Ml4qwroswJypZf1Nxz',
                'category': cat_map['gadgets'],
                'author': auth_map['प्रिया देसाई'],
                'meta_title': '34-इंच अल्ट्रावाइड मॉनिटर कोडिंग रिव्यू (8.9/10)',
                'meta_description': 'दोहरे मॉनिटर्स बनाम सिंगल कर्व्ड डिस्प्ले का व्यावहारिक तुलनात्मक परीक्षण।',
                'schema_type': 'Product',
                'rating': 8.9,
                'product_price': '₹38,990',
                'reading_time_minutes': 5,
                'views_count': 26800,
                'tags': ['MacBookM3'],
            },
            # Trending 01
            {
                'title': 'पायथन में 10 उपयोगी वन-लाइनर कोड्स',
                'slug': 'python-10-useful-one-liner-codes',
                'excerpt': 'स्वैपिंग, लिस्ट कॉम्प्रिहेंशन और डिक्शनरी मर्जिंग के स्मार्ट वन-लाइनर्स।',
                'content': '10 जादुई पायथन वन-लाइनर्स जो कोड को 5 गुना छोटा बनाते हैं।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCVGA-2QQnMT-PE1ik55ILeJYxl3OeRDHVkyZTwW7_-TSmBT-PDyMvNoAPdXn67VSAQW61Uk79flmrQu47QIxAPTE9NBsShZf7-YO7f-bvTl1pgtMasCbac8BGVgmWd5dUy3MYcuklqHd7FARO7JEwdtqqkJsDWLyns0yKSCgXP-ah21vXjIzyhDe3Cb8ml14MAHa5V8f05Okx4dcI8Rcr_KtCP99JHZVzXM_P0xafRLnau1vi6MWC-',
                'category': cat_map['programming'],
                'author': auth_map['विक्रम राठौर'],
                'meta_title': '10 जादुई पायथन वन-लाइनर्स – कोड छोटा और तेज बनाएं',
                'meta_description': 'डेवलपर्स के लिए सबसे उपयोगी पायथन वन-लाइनर्स।',
                'is_trending': True,
                'reading_time_minutes': 3,
                'views_count': 39500,
                'tags': ['Python'],
            },
            # Trending 02
            {
                'title': 'God Mode कैसे एक्टिवेट करें विंडोज 11 में',
                'slug': 'how-to-activate-god-mode-windows-11',
                'excerpt': 'कंट्रोल पैनल के सभी 200+ छिपे हुए सेटिंग्स को एक ही फोल्डर में लाएं।',
                'content': 'डेस्कटॉप पर न्यू फोल्डर बनाएं और नाम GodMode.{ED7BA470-8E54-465E-825C-99712043E01C} रखें।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuD8jm8gZK_Lq7LMNOT566p7wm1DhgHm7bgb09ho1zEmYBYqQcP2P756xUijnydp9GmyHm3W8wdnn-QiuJGrQ7i2qLUt-S2eLMY5oOjborQ9A9N97tMmPZUYQtSLJrWoDyyTM2iFPeUTm6klm7JZRNC6Sju-eNi1VVqAIVx4brgy12THkv9U2PYQrwrQDrBvQHYtqDUwAwAXGIWTgN0Yi5nhmhVEv-9MUJaeIsEowSYfLx5Hc1vPNvn1',
                'category': cat_map['computer-tricks'],
                'author': auth_map['राहुल शर्मा'],
                'meta_title': 'विंडोज 11 में God Mode कैसे ऑन करें',
                'meta_description': '200+ गुप्त कंट्रोल पैनल सेटिंग्स एक क्लिक में खोलें।',
                'is_trending': True,
                'reading_time_minutes': 2,
                'views_count': 35100,
                'tags': ['Windows11'],
            },
            # Trending 03
            {
                'title': 'ChatGPT कोडिंग प्रॉम्प्ट्स: 10 गुना तेज़ कोड लिखें',
                'slug': 'chatgpt-coding-prompts-10x-faster-software',
                'excerpt': 'डीबगिंग, यूनिट टेस्ट लिखने और रेगुलर एक्सप्रेशन बनाने के सिद्ध प्रॉम्प्ट्स।',
                'content': 'सॉफ्टवेयर आर्किटेक्ट्स द्वारा दैनिक उपयोग किए जाने वाले टॉप 10 ChatGPT प्रॉम्प्ट्स।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuC6pyGt62aZVGw-g74gEMnxw-bRfBBb5IOFKYMs3CBUonSj_JpxL3j7Z-lK5CW-R3mJv4nC1JBlWI5vWFINsK1TZdQWXf1ykmtHPQc1fmlhDey-v0xMd5pEugYL7qaRgtTT3bnwp5yXnSGqfX3fLfLi8qaYd2SxEyE-mUvHvugiYtTnFAjV7AGwjqokl_Dsw7a2pCAQYCP3W4aupqrM0WN3JGDbnRvMVTGn_RK9UGDTPlYgayHRu99M',
                'category': cat_map['programming'],
                'author': auth_map['विक्रम राठौर'],
                'meta_title': 'ChatGPT कोडिंग प्रॉम्प्ट्स – डेवलपर प्रोडक्टिविटी 10x',
                'meta_description': 'डीबगिंग और यूनिट टेस्टिंग के लिए सिद्ध एआई प्रॉम्प्ट्स।',
                'is_trending': True,
                'reading_time_minutes': 4,
                'views_count': 42100,
                'tags': ['AIटूल्स'],
            },
            # Trending 04
            {
                'title': 'पुराने लैपटॉप में SSD लगाकर स्पीड 5x बढ़ाएं',
                'slug': 'boost-old-laptop-speed-5x-with-ssd-upgrade',
                'excerpt': 'HDD से SSD पर विंडोज क्लोन करने का सुरक्षित और आसान तरीका।',
                'content': 'केवल ₹2000 खर्च करके 5 साल पुराने सुस्त लैपटॉप को सुपरफास्ट बनाएं।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAQQ2DWYgbs7Pdel_eAcgN81m67z-IyPTzWvG4acXiCmGkcH-ioM9hT-PQ05mpjMbzVmYPlhgNOBHmdatpnDSKfRuCkvpC99A7BK33cwxorsrLzaZEoLy-SVXRrrBTBecxtX3ZiKC_Smz7jmMBb3Mc4l1iyUA3nhH54DzHDXB_ks4jOwCaYOj0oyDB4Vm_lmKXGMxIWzUW5_CQJ6xbeSdKbOdseNgXIkxL1_fm4FkABDK3u8YLPvfM_',
                'category': cat_map['gadgets'],
                'author': auth_map['अमन वर्मा'],
                'meta_title': 'लैपटॉप में SSD अपग्रेड गाइड – 5x स्पीड बूस्ट',
                'meta_description': 'HDD से SSD पर विंडोज क्लोन करने का सुरक्षित और आसान तरीका।',
                'is_trending': True,
                'reading_time_minutes': 5,
                'views_count': 29800,
                'tags': ['Windows11'],
            },
            # Trending 05
            {
                'title': 'वाई-फाई को सुरक्षित रखने के 5 आसान उपाय',
                'slug': '5-easy-steps-to-secure-home-wifi-network',
                'excerpt': 'डिफ़ॉल्ट पासवर्ड बदलना, WPA3 सुरक्षा और गेस्ट नेटवर्क सेट करना।',
                'content': 'हैकरों और अनधिकृत पड़ोसियों से अपने होम राउटर को सुरक्षित करने की आसान हिंदी गाइड।',
                'cover_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuBgeaTQTPi3OPPvEFEGipcQoUFCjm4fs8aUhUFa7rJow51XiJ4vSW43vj1ZmIjJkiuJsfw4H-f0BcohQ2ybl0o3mAmSK3TaFueNuLnqpFxkm2MfrcV-J9RwVlDZg3ngCe1vrK4Tq6-1KPSsoSQn9bnbjy6tFHFCWIN96MFK69Jdi6HxjuvsdL6lUwE38sQ3zaa1ub4OaQwjYfHlTvvdLpobyJTqB1aaQWTjiMkVb63Yz0Yt19qWYWzU',
                'category': cat_map['computer-tricks'],
                'author': auth_map['राहुल शर्मा'],
                'meta_title': 'होम वाई-फाई नेटवर्क कैसे सुरक्षित करें – 5 आसान टिप्स',
                'meta_description': 'WPA3 एन्क्रिप्शन और गेस्ट नेटवर्क सेटिंग गाइड।',
                'is_trending': True,
                'reading_time_minutes': 3,
                'views_count': 21300,
                'tags': ['CyberSecurity'],
            },
        ]

        count = 0
        for item in articles_data:
            tag_names = item.pop('tags', [])
            art, created = Article.objects.get_or_create(slug=item['slug'], defaults=item)
            if created or art.tags.count() == 0:
                for t_name in tag_names:
                    if t_name in tag_map:
                        art.tags.add(tag_map[t_name])
            count += 1

        # 5. Static Pages
        StaticPage.objects.get_or_create(
            slug='about',
            defaults={
                'title': 'हमारे बारे में',
                'content': 'टेकवाणी भारत का अग्रणी हिंदी टेक पोर्टल है जहां आपको प्रामाणिक टेक ज्ञान सरल हिंदी में मिलता है।',
                'meta_title': 'हमारे बारे में (About Us) – टेकवाणी हिंदी टेक मैगज़ीन',
                'meta_description': 'जानिए टेकवाणी की यात्रा, हमारा उद्देश्य, और हमारी संपादकीय टीम।',
            }
        )
        StaticPage.objects.get_or_create(
            slug='privacy-policy',
            defaults={
                'title': 'गोपनीयता नीति',
                'content': 'टेकवाणी पर हम आपके डेटा और कुकीज़ की पूर्ण सुरक्षा सुनिश्चित करते हैं।',
                'meta_title': 'गोपनीयता नीति (Privacy Policy) – टेकवाणी',
                'meta_description': 'टेकवाणी की आधिकारिक गोपनीयता नीति, कुकीज और सुरक्षा दिशानिर्देश।',
            }
        )

        self.stdout.write(self.style.SUCCESS(f"✓ बधाई! सभी {count} आर्टिकल्स, 7 कैटेगरीज, 4 लेखक और पेजेस सफलतापूर्वक लोड हो गए।"))
