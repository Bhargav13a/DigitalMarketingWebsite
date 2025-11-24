from django.shortcuts import render

def home(request):

    services = [
        ("Social Media Marketing & Management", "We manage and grow your online presence with creative strategy and daily content."),
        ("Content Marketing", "High-quality written and visual content designed to engage your target audience."),
        ("Email Marketing & Automation", "Automated, personalized email flows that bring repeat conversions."),
        ("Paid Social Advertising", "Targeted ad campaigns on Meta, Google & more for high ROI."),
        ("Online Reputation Management", "Monitor and manage your brand presence across the internet."),
        ("Branding & Re-branding", "Complete brand identity creation with visuals, messaging & strategy."),
        ("E-commerce Marketing", "Boost conversions and sales for your online store using smart funnels."),
        ("App Store Optimisation", "Improve app visibility & ranking on Play Store and App Store."),
        ("Influencer Marketing", "Authentic creator collaborations for brand amplification."),
        ("Video Production & Marketing", "High-quality video ads, reels, and promotional content."),
        ("Marketplace & Channel Marketing", "Scale your business across Amazon, Flipkart, Meesho, etc.")
    ]

    context = {
        "services": services,
        'company_name': 'Buzz Craft Socials',
        'slogan': 'Choose Buzz Craft Socials to promote your business',

        'financials': {
            'revenue': [
                ('Starter Plan', 6, 12000, 72000, 864000),
                ('Growth Plan', 4, 25000, 100000, 1200000),
                ('Premium Plan', 2, 55000, 110000, 1320000),
            ],
            'addons_annual': 600000,
            'total_revenue': 4000000,
            'expenses_annual': 2280000,
            'net_profit': 1720000,
            'growth': [
                ('Year 1', 4000000, None, '43%'),
                ('Year 2', 7000000, '+75%', '45%'),
                ('Year 3', 10000000, '+45%', '50%'),
            ]
        },

        'contact': {
            'email': 'hello@yourdomain.com',
            'phone': '+91 98765 43210',
            'address': '123 Marketing Lane, Ahmedabad, India',
            'instagram': 'https://instagram.com/yourhandle',
            'linkedin': 'https://linkedin.com/company/yourcompany'
        }
    }

    return render(request, "main/home.html", context)
