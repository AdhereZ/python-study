from lxml import etree

xml="""
      <div>
        <li id="1">1</li>
        <li id="2">2</li>
        <li id="3">3</li>
        <li class="4">4</li>
        <span>suv</span>
        <div>gg</div>
        <div>
        <li class="5">5</li>
         <div>
        <li class="6">6</li>
        </div>
        </div>
         <span>
        <li class="7">7</li>
        </span>
    </div>
  """
tree=etree.XML(xml)
# res=tree.xpath("/div") #根节点
# res=tree.xpath("/div/span/text()") #text()表示拿文本
# res=tree.xpath("/div/li/text()")
# res=tree.xpath("/div//li/text()") #取全部后代
res=tree.xpath("/div/*/li/text()")  # *是任意的节点，通配符

print(res)
