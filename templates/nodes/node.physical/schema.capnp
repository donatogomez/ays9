
@0xe4cc0eaf841a7cfa;
struct Schema {
	description @0 :Text;
	ports @1 :List(Text);
	ipPublic @2 :Text;
	sshLogin @3 :Text;
	sshPassword @4 :Text;
	sshkey @5 :Text;
	sshAddr @6 :Text;
	sshPort @7 :Int64 = 0;

}
