import models
import stores
member_store=MemberStore()
post_store=PostsStore()
member1=Member("ahmed",23)
member_store.add(member1)
member2=Member("omar",24)
member_store.add(member2)

post1=Post("greatings","hello this is my first" )
post2=Post("greatings","hello this is my first" )
post3=Post("greatings","hello this is my first" )

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
