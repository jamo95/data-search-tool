test_quit_output = """Welcome to Search
Type 'quit' to exit at any time, Press 'Enter' to continue


    Select search options:
    * Press 1 to search
    * Press 2 to view a list of searchable fields
    Type 'quit' to exit
    Select search options:


"""

test_view_search_fields_output = """Welcome to Search
Type 'quit' to exit at any time, Press 'Enter' to continue


    Select search options:
    * Press 1 to search
    * Press 2 to view a list of searchable fields
    Type 'quit' to exit
    Select search options:


---------------------------------------------
Search Users with
_id
url
external_id
name
alias
created_at
active
verified
shared
locale
timezone
last_login_at
email
phone
signature
organization_id
tags
suspended
role


---------------------------------------------
Search Tickets with
_id
url
external_id
created_at
type
subject
description
priority
status
submitter_id
assignee_id
organization_id
tags
has_incidents
due_at
via
requester_id


---------------------------------------------
Search Organizations with
_id
url
external_id
name
domain_names
created_at
details
shared_tickets
tags


Enter any input to restart or enter quit to exit


"""

test_search_user_output = """Welcome to Search
Type 'quit' to exit at any time, Press 'Enter' to continue


    Select search options:
    * Press 1 to search
    * Press 2 to view a list of searchable fields
    Type 'quit' to exit
    Select search options:


Select 1) Users or 2) Tickets or 3) Organizations
Enter search term
Enter search value
_id                      19
url                      http://initech.zendesk.com/api/v2/users/19.json
external_id              68e35e26-7b1f-46ec-a9e5-3edcbcf2aeb9
name                     Francis Rodrigüez
alias                    Mr Lea
created_at               2016-05-05T01:56:24 -10:00
active                   False
verified                 False
shared                   False
locale                   zh-CN
timezone                 Brazil
last_login_at            2012-05-25T01:55:34 -10:00
phone                    8275-873-442
signature                Don't Worry Be Happy!
organization_id          124
tags                     ['Vicksburg', 'Kilbourne', 'Gorham', 'Gloucester']
suspended                False
role                     agent


Enter any input to restart or enter quit to exit


"""

test_search_tickets_output = """Welcome to Search
Type 'quit' to exit at any time, Press 'Enter' to continue


    Select search options:
    * Press 1 to search
    * Press 2 to view a list of searchable fields
    Type 'quit' to exit
    Select search options:


Select 1) Users or 2) Tickets or 3) Organizations
Enter search term
Enter search value
_id                      ccf4c82c-f572-4fd2-82a6-11d6055929b8
url                      http://initech.zendesk.com/api/v2/tickets/ccf4c82c-f572-4fd2-82a6-11d6055929b8.json
external_id              badc534c-9f11-45a9-93f2-509b86ed31fa
created_at               2016-01-20T12:45:55 -11:00
type                     problem
subject                  A Catastrophe in Lebanon
description              Nisi elit minim excepteur qui. Non incididunt culpa dolor nostrud est ullamco sunt elit duis amet anim.
priority                 high
status                   hold
submitter_id             35
assignee_id              52
organization_id          110
tags                     ['Ohio', 'Pennsylvania', 'American Samoa', 'Northern Mariana Islands']
has_incidents            True
due_at                   2016-08-14T10:58:25 -10:00
via                      chat


_id                      e804d348-2317-43b2-882a-b29d1a8acc94
url                      http://initech.zendesk.com/api/v2/tickets/e804d348-2317-43b2-882a-b29d1a8acc94.json
external_id              93b1c5a2-3811-464e-9091-77432a8599fc
created_at               2016-07-05T07:25:54 -10:00
type                     problem
subject                  A Nuisance in Grenada
description              Sunt do mollit deserunt do fugiat. Id Lorem voluptate officia do.
priority                 urgent
status                   solved
submitter_id             35
assignee_id              59
organization_id          113
tags                     ['South Dakota', 'Montana', 'District Of Columbia', 'Wisconsin']
has_incidents            False
due_at                   2016-08-06T03:25:46 -10:00
via                      chat


_id                      7382ad0e-dea7-4c8d-b38f-cbbf016f2598
url                      http://initech.zendesk.com/api/v2/tickets/7382ad0e-dea7-4c8d-b38f-cbbf016f2598.json
external_id              6d3b0e05-6013-4513-9913-0bb6a0f66ef7
created_at               2016-03-31T03:16:52 -11:00
type                     task
subject                  A Problem in American Samoa
description              Excepteur dolor in commodo minim irure laboris. In incididunt mollit veniam pariatur ullamco laborum ullamco aliqua do fugiat Lorem.
priority                 high
status                   closed
submitter_id             35
assignee_id              64
organization_id          118
tags                     ['Missouri', 'Alabama', 'Virginia', 'Virgin Islands']
has_incidents            True
due_at                   2016-08-06T08:36:17 -10:00
via                      chat


Enter any input to restart or enter quit to exit


"""

test_search_organizations_output = """Welcome to Search
Type 'quit' to exit at any time, Press 'Enter' to continue


    Select search options:
    * Press 1 to search
    * Press 2 to view a list of searchable fields
    Type 'quit' to exit
    Select search options:


Select 1) Users or 2) Tickets or 3) Organizations
Enter search term
Enter search value
_id                      101
url                      http://initech.zendesk.com/api/v2/organizations/101.json
external_id              9270ed79-35eb-4a38-a46f-35725197ea8d
name                     Enthaze
domain_names             ['kage.com', 'ecratic.com', 'endipin.com', 'zentix.com']
created_at               2016-05-21T11:10:28 -10:00
details                  MegaCorp
shared_tickets           False
tags                     ['Fulton', 'West', 'Rodriguez', 'Farley']


_id                      102
url                      http://initech.zendesk.com/api/v2/organizations/102.json
external_id              7cd6b8d4-2999-4ff2-8cfd-44d05b449226
name                     Nutralab
domain_names             ['trollery.com', 'datagen.com', 'bluegrain.com', 'dadabase.com']
created_at               2016-04-07T08:21:44 -10:00
details                  Non profit
shared_tickets           False
tags                     ['Cherry', 'Collier', 'Fuentes', 'Trevino']


_id                      103
url                      http://initech.zendesk.com/api/v2/organizations/103.json
external_id              e73240f3-8ecf-411d-ad0d-80ca8a84053d
name                     Plasmos
domain_names             ['comvex.com', 'automon.com', 'verbus.com', 'gogol.com']
created_at               2016-05-28T04:40:37 -10:00
details                  Non profit
shared_tickets           False
tags                     ['Parrish', 'Lindsay', 'Armstrong', 'Vaughn']


_id                      104
url                      http://initech.zendesk.com/api/v2/organizations/104.json
external_id              f6eb60ad-fe37-4a45-9689-b32031399f93
name                     Xylar
domain_names             ['anixang.com', 'exovent.com', 'photobin.com', 'marqet.com']
created_at               2016-03-21T10:11:18 -11:00
details                  MegaCörp
shared_tickets           False
tags                     ['Hendricks', 'Mclaughlin', 'Stephens', 'Garner']


_id                      105
url                      http://initech.zendesk.com/api/v2/organizations/105.json
external_id              52f12203-6112-4fb9-aadc-70a6c816d605
name                     Koffee
domain_names             ['farmage.com', 'extrawear.com', 'bulljuice.com', 'enaut.com']
created_at               2016-06-06T02:50:27 -10:00
details                  MegaCorp
shared_tickets           False
tags                     ['Jordan', 'Roy', 'Mckinney', 'Frost']


_id                      106
url                      http://initech.zendesk.com/api/v2/organizations/106.json
external_id              2355f080-b37c-44f3-977e-53c341fde146
name                     Qualitern
domain_names             ['gology.com', 'myopium.com', 'synkgen.com', 'bolax.com']
created_at               2016-07-23T09:48:02 -10:00
details                  Artisân
shared_tickets           False
tags                     ['Nolan', 'Rivas', 'Morse', 'Conway']


_id                      108
url                      http://initech.zendesk.com/api/v2/organizations/108.json
external_id              be72663b-338d-42f4-bd52-cf6584cad674
name                     Zolarex
domain_names             ['elemantra.com', 'zizzle.com', 'miraclis.com', 'overplex.com']
created_at               2016-07-26T09:35:57 -10:00
details                  Non profit
shared_tickets           False
tags                     ['Rosales', 'Middleton', 'Garrett', 'Page']


_id                      109
url                      http://initech.zendesk.com/api/v2/organizations/109.json
external_id              5f930931-37fd-41a2-9c68-1cd5b99e7a3e
name                     Möreganic
domain_names             ['pearlesex.com', 'netility.com', 'rodemco.com', 'cuizine.com']
created_at               2016-06-03T10:50:56 -10:00
details                  MegaCorp
shared_tickets           False
tags                     ['Price', 'Meyer', 'Heath', 'Skinner']


_id                      112
url                      http://initech.zendesk.com/api/v2/organizations/112.json
external_id              32e979ff-47b4-43b9-8b74-eea1227905d9
name                     Quilk
domain_names             ['valreda.com', 'strozen.com', 'signity.com', 'quantasis.com']
created_at               2016-01-10T03:21:25 -11:00
details                  MegaCorp
shared_tickets           False
tags                     ['Hall', 'Dorsey', 'Shepard', 'Carter']


_id                      115
url                      http://initech.zendesk.com/api/v2/organizations/115.json
external_id              71010066-113a-48b5-8498-184ae2c72f93
name                     Netur
domain_names             ['tubalum.com', 'imaginart.com', 'olucore.com', 'uniworld.com']
created_at               2016-07-25T01:19:05 -10:00
details                  Artisan
shared_tickets           False
tags                     ['Wilkerson', 'Knight', 'Stephenson', 'Witt']


_id                      116
url                      http://initech.zendesk.com/api/v2/organizations/116.json
external_id              dbc692fc-e1ae-47d8-a1d7-263d07710fe1
name                     Zentry
domain_names             ['datagene.com', 'exoteric.com', 'beadzza.com', 'digiprint.com']
created_at               2016-01-13T09:34:07 -11:00
details                  Artisan
shared_tickets           False
tags                     ['Schneider', 'Hoover', 'Wilcox', 'Hewitt']


_id                      118
url                      http://initech.zendesk.com/api/v2/organizations/118.json
external_id              6970300e-f211-4c01-a538-70b4464a1d84
name                     Limozen
domain_names             ['otherway.com', 'rodeomad.com', 'suremax.com', 'fishland.com']
created_at               2016-02-11T04:24:09 -11:00
details                  MegaCorp
shared_tickets           False
tags                     ['Leon', 'Ferguson', 'Olsen', 'Walsh']


_id                      119
url                      http://initech.zendesk.com/api/v2/organizations/119.json
external_id              2386db7c-5056-49c9-8dc4-46775e464cb7
name                     Multron
domain_names             ['bleeko.com', 'pulze.com', 'xoggle.com', 'sultraxin.com']
created_at               2016-02-29T03:45:12 -11:00
details                  Non profit
shared_tickets           False
tags                     ['Erickson', 'Mccoy', 'Wiggins', 'Brooks']


_id                      120
url                      http://initech.zendesk.com/api/v2/organizations/120.json
external_id              82da5daf-d6ad-484d-a831-05cd3e2baea5
name                     Andershun
domain_names             ['valpreal.com', 'puria.com', 'bostonic.com', 'roughies.com']
created_at               2016-01-15T04:11:08 -11:00
details                  MegaCorp
shared_tickets           False
tags                     ['Robinson', 'Santana', 'Whitehead', 'England']


_id                      125
url                      http://initech.zendesk.com/api/v2/organizations/125.json
external_id              42a1a845-70cf-40ed-a762-acb27fd606cc
name                     Strezzö
domain_names             ['techtrix.com', 'teraprene.com', 'corpulse.com', 'flotonic.com']
created_at               2016-02-21T06:11:51 -11:00
details                  MegaCorp
shared_tickets           False
tags                     ['Vance', 'Ray', 'Jacobs', 'Frank']


Enter any input to restart or enter quit to exit


"""
