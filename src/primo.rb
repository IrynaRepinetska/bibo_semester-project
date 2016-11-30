require 'exlibris-primo'
search = Exlibris::Primo::Search.new(:base_url => "http://www.aub.aau.dk/primo/", :institution => "AUB", :page_size => "20")
search.add_query_term "xml", "title", "exact"
p search
#count = search.size #=> 20+ (assuming there are 20+ records with this isbn)
#p count
#facets = search.facets #=> Array of Primo facets
#records = search.records #=> Array of Primo records
#records.size #=> 20 (assuming there are 20+ records with this isbn)
#records.each do |record_id, record|
#  holdings = record.holdings #=> Array of Primo holdings
#  fulltexts = record.fulltexts #=> Array of Primo full texts
#  table_of_contents = record.table_of_contents #=> Array of Primo tables of contents
#  related_links = record.related_links #=> Array of Primo related links
#end
