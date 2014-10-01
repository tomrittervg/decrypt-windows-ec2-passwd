require 'base64'
require 'openssl'
require 'pathname'
require 'trollop' # gem install trollop

opts = Trollop::options do
  opt :key_path, "Path to private key pem file", type: :string
  opt :password_data, "Base64-encoded password_data as returned by EC2::GetPasswordData operation (strip newlines)", type: :string
end

pem_bytes = Pathname.new(opts[:key_path]).read
private_key = OpenSSL::PKey::RSA.new pem_bytes
pd = Base64.decode64 opts[:password_data]
puts "Password: #{private_key.private_decrypt pd}"
exit 0
