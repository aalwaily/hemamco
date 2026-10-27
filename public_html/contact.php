<?php
/**
 * EDIT THE VALUES BELOW THIS LINE TO ADJUST THE CONFIGURATION
 */

// All enquiries are delivered to this address.
$mailTo     = 'info@hemamco.com';

// Fixed sender address on your own domain. Visitor input is NEVER used as the
// sender; their address goes into Reply-To after validation instead.
$mailFrom   = 'website@hemamco.com';

$successMsg = 'Thank you, your message has been sent successfully!';
$fillMsg    = 'Please fill all fields!';
$errorMsg   = 'Sorry, there was a problem sending your message. Please email info@hemamco.com.';
$emailMsg   = 'Please enter a valid email address!';

// Arabic versions, used when the form is sent from an Arabic page (lang=ar).
$successMsgAr = 'شكرًا لك، تم إرسال رسالتك بنجاح!';
$fillMsgAr    = 'يرجى تعبئة جميع الحقول المطلوبة.';
$errorMsgAr   = 'عذرًا، حدثت مشكلة أثناء إرسال رسالتك. يرجى مراسلتنا على info@hemamco.com.';
$emailMsgAr   = 'يرجى إدخال بريد إلكتروني صحيح.';

/**
 * DO NOT EDIT ANYTHING BELOW THIS LINE, UNLESS YOU'RE SURE WHAT YOU'RE DOING
 */

header('Content-Type: application/json; charset=utf-8');

function respond($type, $msg) {
	echo json_encode(array('type' => $type, 'msg' => $msg));
	exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
	http_response_code(405);
	respond('error', 'Invalid request.');
}

// Read a field, trim it and cap its length.
function field($name, $max) {
	$v = isset($_POST[$name]) && is_string($_POST[$name]) ? trim($_POST[$name]) : '';
	return function_exists('mb_substr') ? mb_substr($v, 0, $max, 'UTF-8') : substr($v, 0, $max);
}

// Values that end up in mail headers must be single-line: strip CR, LF and
// other control characters so nobody can inject extra headers (Bcc:, To: ...).
function header_safe($v) {
	return trim(preg_replace('/[\x00-\x1F\x7F]+/u', ' ', $v));
}

if (isset($_POST['lang']) && $_POST['lang'] === 'ar') {
	$successMsg = $successMsgAr;
	$fillMsg    = $fillMsgAr;
	$errorMsg   = $errorMsgAr;
	$emailMsg   = $emailMsgAr;
	$isArabic   = true;
} else {
	$isArabic   = false;
}

$name    = header_safe(field('name', 100));
$email   = header_safe(field('email', 254));
$phone   = header_safe(field('phone', 40));
$subject = header_safe(field('subject', 150));
$message = field('message', 5000);

$labels  = array('Name' => $name, 'Email' => $email, 'Phone' => $phone, 'Subject' => $subject, 'Message' => $message);
$missing = array_keys(array_filter($labels, function ($v) { return $v === ''; }));

if (count($missing) === count($labels)) {
	respond('error', $fillMsg);
}
if ($missing) {
	respond('error', $isArabic ? $fillMsg : 'Please fill ' . implode(', ', $missing) . ' fields!');
}
if (filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
	respond('error', $emailMsg);
}

$body  = "New enquiry from the Hemamco website\r\n\r\n";
$body .= "Name: " . $name . "\r\n";
$body .= "Email: " . $email . "\r\n";
$body .= "Phone: " . $phone . "\r\n";
$body .= "Subject: " . $subject . "\r\n";
$body .= "Language: " . ($isArabic ? 'Arabic' : 'English') . "\r\n\r\n";
$body .= "Message:\r\n" . str_replace(array("\r\n", "\r"), "\n", $message) . "\r\n";

// RFC 2047-encode the subject so Arabic text survives.
$mailSubject = '=?UTF-8?B?' . base64_encode('Website enquiry: ' . $subject) . '?=';

$headers  = 'From: Hemamco Website <' . $mailFrom . ">\r\n";
$headers .= 'Reply-To: ' . $email . "\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "Content-Transfer-Encoding: 8bit";

$success = @mail($mailTo, $mailSubject, $body, $headers, '-f' . $mailFrom);

respond($success ? 'success' : 'error', $success ? $successMsg : $errorMsg);
