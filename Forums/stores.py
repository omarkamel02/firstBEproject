class MemberStore:

  members = []
  last_id=1
  def get_all(self):
     return members

  def add(self, member):
      member.id = MemberStore.last_id

  	  MemberStore.members.append(member)

  	  MemberStore.last_id += 1
  def get_by_id(self, id):
      # search for member by id
      for mem in MemberStore.members :
          if mem.id == id:
              return mem
          else :
              return 0



  def update(self, member):
     # update member data
     name=get_by_id(member.id)
     name=member


  def delete(self, id):
      # delete member by id
      name=get_by_id(id)
      MemberStore.members.remove(name)

  def entity_exists(self, member):
      # checks if an entity exists in a store
      if get_by_id(member.id) not 0:
          return True
      else :
          return False
 def get_by_name (self,name):
     for member in MemberStore.members:
         if member.name==name:
             return member 

class PostsStore:

  posts = []

  def get_all(self):
     return posts

  def add(self, post):
      members.append(post)

  def get_by_id(self, id):
      # search for member by id

  def update(self, post):
     # update member data

  def delete(self, id):
      # delete member by id

  def entity_exists(self, post):
      # checks if an entity exists in a store
